#---------------------------------------------
# Written by Sarah Morgan (sjmorgan@mit.edu, sjmorgan162@gmail.com)
# This code is a result of my (Sarah Morgan's) SM thesis here: [[3]](#3). Several case studies are shown there with a more in-depth discussion of this procedure of adaptable maneuver planning. 
# © Massachusetts Institute of Technology 2021.
# Based Upon Prior Work by Dr McGrath's 2019 IAC paper (IAC-19-B4.3.10)
#(Satellite characteristics, initial orbits, and target locations came from that paper)
#-----------------------------------------------    
def series_of_maneuvers(dV1, dV2, dV3, disp_flag):
    
    
    #-------------------------------------------------------------------------
    ### IMPORTS ###
    #-------------------------------------------------------------------------
    #local files needed
    from distance_SSP_to_target import distance_SSP_to_target
    from load_hurricane_data import import_hurricane
    from lowering_maneuver import lowering_maneuver
    from raising_maneuver import raising_maneuver
    from propagate import propagate
    
    #Other python packages needed
    import math
    import numpy as np
    import networkx as nx
    import datetime
    import os

    #-------------------------------------------------------------------------
    ### INPUTS ###
    #-------------------------------------------------------------------------
    #delta-V for each manuever given as an input 
    #- the number of values corresponds to the number of manuevers which is equal to the number of targets
    #delta-V stored here
    dV_list = [[dV1, dV2, dV3]]
    
    
    ###Initialize satellites--------------------------------------------------
    #A list of lists is used to store satellite(s) states and their 
    #maneuver info, and target access information 
    num_sats = 1
    
    #epoch Oct 10, 2010, 12:00 UTC
    date_epoch = datetime.datetime(2010,10,10,12)
    
    #note that AOL and RAAN at epoch start are used as opposed to RAAN and argument of perigee
    sat_elems = ['Satellite Number', 'Semi-major Axis (m)', 'Inclination (deg)',\
                 'RAAN (deg)', 'Argument of Latitude (deg)', 'RA at Epoch Start (deg)', \
                 'SSP Lat. (deg)', 'SSP Lon. (deg)', \
                 'Time Since Epoch (sec)', \
                 'Delta-V Used in current maneuver', 
                 'Dist to Current Target (km)']
    satellites = []
    
    for i in range(num_sats):
        semi_major_axis = 7074000 #m
        incl = 40 #deg
        RAAN0 = 0+20*i #deg - this means for multiple satellites, satellites are spaced by 20 deg RAAN
        u0 = 0 #deg
        RAepoch = -161.155 #deg
        satellites.append([i, semi_major_axis, incl, \
                           RAAN0, u0, RAepoch, \
                           0, 0, \
                           0, 0,\
                           0,\
                           0])
       #note the ssp, delt-V and dist to target are initially clear
    
    if disp_flag==1:
        print('---')
        print('Satellite(s) initial states:')
        print('---')
        for i in range(num_sats):
            for x in range(len(sat_elems)):
                print(sat_elems[x],x,':\t', satellites[i][x])
            print('---')
    
    #this is the max acceleration available on the satellite
    satellite_mass = 4 #kg
    max_thrust = 0.35*10**(-3) #N
    accel = max_thrust/satellite_mass #m/s^2
    
    ###Initialize Targets-----------------------------------------------------
    
    num_targets = len(dV_list[0])
    targets = []
    
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'target_tracks\megi_data.xlsx') #(!) path may need to be changed for non-Windows users
    #These are locations of the eye of Typhoon Megi (2010)
    target_interval = 2.5*24*3600 #sec
    targets_time,targets_lat,targets_long, time_since_epoch, latitude, longitude = import_hurricane(file, date_epoch, num_targets, target_interval)
    targets = [[targets_time[i], targets_lat[i], targets_long[i]] for i in range(num_targets)]
    
    #Time window corresponds to allowed viewing time around each target (ie +/- 20 hrs target time)
    time_window = 20*3600 #sec
    
    #Establishes minimum acceptable distance to eye of the storm 
    min_distance_to_eye = 100000 #m
    
    
    #-------------------------------------------------------------------------
    ### PARAMETERS ###
    #-------------------------------------------------------------------------
    #Model Parameters---------------------------------------------------------
    mu = 3.98600*10**14         # standard gravitational parameter, m^3/s^2
    Re = 6371000                # mean Earth radius, m
    J2 = 1082.7*(10**-6)        # coefficient of the Earth's gravitational zonal harmonic of the 2nd degree
    vel_e = 7.29212*10**(-5)    # angular velocity of the earth, rad/s
    rad = math.pi/180           # conversion of deg to rad
    flattening = 0.00335281     # flattening factor of the earth
    time_step = 10              # propagation time step (for viewing window propagation)
    
    
    #-------------------------------------------------------------------------
    ### CODE START ###
    #-------------------------------------------------------------------------
    #Satellite state is stored in dictionary nodes, and node numbers themselves in Graph G
    nodes = {0: satellites}
    G = nx.Graph()
    if disp_flag==1:
        print("Executing maneuvers...")
    
    #the node we are starting to pull from
    origin_node = 0
    # the node we are creating
    current_node = 1
    
    #the information we start with
    old_sat_list = nodes[origin_node].copy()
    calc_nodes_last_target = [0]
    num_target = 0 #start with first target in list
    
    
    calc_nodes_current_target = []
    for target in targets:
        num_target = num_target +1;
        
        solution_found = False
        
        #Define viewing window for each target
        time_min = target[0] - time_window;        
        time_max = target[0] + time_window;
        time_list = np.arange(time_min, time_max+time_step, time_step)

        #Interpolate between known track points for the viewing window time
        #this will be used to see if the satellite gets close to the storm
        lat_interp = np.interp(time_list, time_since_epoch, latitude)
        long_interp = np.interp(time_list, time_since_epoch, longitude)
        current_target = [time_list, lat_interp, long_interp]
        
        if disp_flag ==1:
            print('---')
            print("\nChecking accesses for target:"+"\t" + str(num_target))
            print('Target time: ' + str(target[0]/3600/24) + ' days')
            print('Target latitude: ' + str(target[1]) + ' deg')
            print('Target longitude: ' + str(target[2]) + ' deg')
        
        #Create new place to store satellite states
        new_sat_list = []
        for i in range(num_sats):
            new_sat_list.append([])

        # (leftover from tree generation approach)- move from one set of notes to the next            
        for origin in calc_nodes_last_target:
            old_sat_list = nodes[origin].copy()
            #for multiple satellites, each will be manuevered in sequence
            for sat in range(len(old_sat_list)):
                maneuvering_sat = old_sat_list[sat][:]
                sat_time = maneuvering_sat[8]
                
                #Define the vewing window duration for each target, relative to satellite
                duration_min = time_min - sat_time 
                duration_max = time_max - sat_time
                duration_list = np.arange(duration_min, duration_max+time_step, time_step)
                
                
                dV = dV_list[sat][num_target-1]
                #Now execute the maneuvers- either propagate/lower/raise according to the delta-V
                if dV ==0:
                    flag = 'N/A'
                    updated_sat = propagate(mu, Re, J2, vel_e, rad, flattening, maneuvering_sat, accel, duration_min)
                
                if dV<0:
                    flag = 'LOWER'
                    #timing of manuevers (seconds of manuever, propogate, maneuver duration which correspond to the 3 phases can also be stored)
                    [updated_sat, timing] = lowering_maneuver(mu, Re, J2, vel_e, rad, flattening, maneuvering_sat, accel, abs(dV), duration_min)
                    if updated_sat!= None:
                        updated_sat[9] = abs(dV)
                if dV>0:
                    flag = 'RAISE'
                    #timing of manuevers (seconds of manuever, propogate, maneuver duration which correspond to the 3 phases can also be stored)
                    [updated_sat, timing] = raising_maneuver(mu, Re, J2, vel_e, rad, flattening, maneuvering_sat, accel, dV, duration_min)
                    if updated_sat!= None:
                        updated_sat[9] = abs(dV)
                    
                #If the manuever was successful (time was sufficient for the delta-V), updated sat will have been created   
                if updated_sat !=None: 
                    
                    #now propogate the satellite to the end of the time window to see the number/quality of accesses
                    propagate_sat_options = propagate(mu, Re, J2, vel_e, rad, flattening, updated_sat, accel, (duration_list-duration_min))
                    
                    distance = distance_SSP_to_target(mu, Re, rad, propagate_sat_options[6], propagate_sat_options[7], lat_interp, long_interp)
                    num_accesses = 0
                    num_accesses = sum(1 for x in distance if x<min_distance_to_eye )
                        
                    if num_accesses>0:
                        #If the storm was accessed, record the accesses in the 'satellite' list
                        #also maneuver timing can be stored- not currently done
                        access_distance = []
                        index = 0
                        for x in distance:
                            #record number of accesses
                            index = index+1
                            if x<min_distance_to_eye:
                                #record access distance at each possible access:
                                access_distance.append(x)
                                lat = propagate_sat_options[6][index]
                                long = propagate_sat_options[7][index]
                                lateye = lat_interp[index]
                                longeye = long_interp[index]
                                distance = distance_SSP_to_target(mu, Re, rad, lat, long, lateye, longeye)
                                                            
                                totalSeconds = time_min+index*time_step #time since epoch in sec

                                if disp_flag==1:
                                    print('---successful access---')
                                    print('Distance: '+ str(x/1000) + 'km') 
                                    print('Current Time: '+ str(datetime.datetime(2010,10,10,12)+ datetime.timedelta(seconds=totalSeconds)) + 'UTC')
                                    print('Hurricane: Lat. '+ str(lat) + ' deg  Long. ' + str(long) + ' deg')
                        #Mark that a solution has been found for this target
                        solution_found = True
                        #Record the mean and minimum access distances
                        mean_distance_pass = sum(access_distance)/num_accesses
                        min_distance_pass = min(access_distance)
                        
                        #Either distance can be saved
                        updated_sat[10] = min_distance_pass
                
                        propagate_sat = propagate(mu, Re, J2, vel_e, rad, flattening, updated_sat, accel, time_window*2)
                        new_sat_list[updated_sat[0]] = propagate_sat
                        nodes[current_node] = new_sat_list.copy()
                        propagate_sat =[]
                        updated_sat = []
                        calc_nodes_current_target.append(current_node)
                        if dV ==0:
                            dV_adj = 0.00001 #to ensure graph is connected (edge length cannot be 0)
                        else:
                            dV_adj = abs(dV) #to ensure graph is connected (edge length cannot be negative)
                            
                        #Leftover from tree generation- add edge and then move on to next node
                        G.add_edge(origin, current_node, dV = dV_adj,dist_to_target = mean_distance_pass,  target_accesses = num_accesses, man_type = flag)
                        current_node = current_node+1
                        
                        if disp_flag==1:
                                    print('---summary of accesses for target ', str(num_target), '---')
                                    print('Mean Distance: '+ str(round(mean_distance_pass/1000,2)) + ' km') 
                                    print('Min Distance: '+ str(round(min_distance_pass/1000,2)) + ' km')
                                    print('Delta-V Used: ' + str(dV) + ' m/s')
                                    print('Total Access Time: ' + str(num_accesses*time_step) + ' s')
                                    print('')
                    
                        
        if solution_found == False:
            #if a solution cannot be found, propogate sat, and record 0 accesses
            if disp_flag==1:
                print('---no access available---')
            for origin in calc_nodes_last_target: 
                old_sat_list = nodes[origin].copy()
                for x in range(len(old_sat_list)):
                    flag = 'N/A'
                    sat =  old_sat_list[x][:]
                    propagate_sat = propagate(mu, Re, J2, vel_e, rad, flattening, sat, accel, duration_max)
                    propagate_sat[10] = 999999
                    new_sat_list[sat[0]] = propagate_sat.copy()
                    nodes[current_node] = new_sat_list.copy()
                    propagate_sat =[]
                    calc_nodes_current_target.append(current_node)
                    G.add_edge(origin, current_node, target_accesses = 0, dV =0.00001, dist_to_target = 999999, man_type = flag)
                    current_node = current_node+1 
        calc_nodes_last_target = calc_nodes_current_target[:]
        calc_nodes_current_target = []
    
    #Leftover from tree generation
    #Tree Generation is complete... finding shortest path:
    complete_path = {}
    #record all possible path lengths
    path = nx.dijkstra_path(G, source=0, target=None, weight='dV')
    #only want the complete paths that view all targets
    for key in path:
        if len(path[key])==num_targets+1:
            current_path = path[key]
            length = nx.dijkstra_path_length(G, source=current_path[0], target=current_path[-1], weight='dV')
            complete_path[length] = current_path
    #then select shortest path
    min_path_length = 9999
    for path_length in complete_path:
        if path_length<min_path_length:
            min_path_length = path_length
            shortest_complete_path = complete_path[path_length]
    shortest_complete_path_edges = zip(shortest_complete_path,shortest_complete_path[1:])
    shortest_complete_path_edges = set(shortest_complete_path_edges)
    
    #Left over from tree generation- record the shortest path information
    dV_total = 0
    num_accesses_total = 0
    dist_sum_length=[]
    for i in shortest_complete_path_edges: 
         dV_total = dV_total + G.edges[i]['dV']
         num_accesses_total = (num_accesses_total + G.edges[i]['target_accesses'])
         if G.edges[i]['dist_to_target']< min_distance_to_eye:
            dist_sum_length.append(G.edges[i]['dist_to_target'])
    if len(dist_sum_length)>0:
        dist_mean = sum(dist_sum_length)/len(dist_sum_length)
    else:
        dist_mean= 99999
    
    total_access_time = num_accesses_total*time_step
    if disp_flag ==1:
        print('---')
        print('Total delta-V used: ', round(dV,2), ' m/s')
        print('Total access time: ', total_access_time, ' s')
        print('Mean distance to storm (across all accesses): ', round(dist_mean/1000,2), ' km')
    
    # For GA use, simply return the summary objectives:
    # Note that the GA assumes minimization of all objectives by default, so a negative total access time is returned
    # (want to minimize dV use, maximize total access time, minimize mean distance)
    # Different objectives could be used here as well (minimum distance)
    return [dV_total, -total_access_time, dist_mean]
