#---------------------------------------------
#Written Summer 2020 by Sarah Morgan (sjmorgan@mit.edu)
#Based Upon Prior Work by Dr McGrath's 2019 IAC paper (IAC-19-B4.3.10)
  
    # Satellite characteristics, initial orbits, and target locations came from that paper
#-----------------------------------------------    
def series_of_maneuvers(dV1, dV2, dV3, dV4, dV5):
    
    from lowering_maneuver import lowering_maneuver
    from raising_maneuver import raising_maneuver
    from propagate import propagate
    
    from distance_SSP_to_target import distance_SSP_to_target
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    import csv
    import time
    from load_hurricane_data import import_hurricane
    import datetime
    #imports below from https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_circular_tree.html
#    try:
#       import pygraphviz
#       from nx.drawing.nx_agraph import graphviz_layout
#    except ImportError:
#       try:
#           import pydot
#           from networkx.drawing.nx_pydot import graphviz_layout
#       except ImportError:
#           raise ImportError("This example needs Graphviz and either "
#                             "PyGraphviz or pydot")

    

    #Model Parameters-------------------------------------------------------------
    mu = 3.98600*10**14;    #    % standard gravitational parameter, m^3/s^2
    Re = 6371000;           #    % mean Earth radius, m
    J2 = 1082.7*(10**-6);     #   % coefficient of the Earth's gravitational zonal harmonic of the 2nd degree
    vel_e = 7.29212*10**(-5);  #  % angular velocity of the earth, rad/s
    rad = math.pi/180;              # % conversion of deg to rad
    flattening = 0.00335281;    #% flattening factor of the earth
    
    
    #%Initialize satellites------------------------------------------------------
    num_sats = 1
    #Orbit Characteristics, maneuver Info, and Target Access Information Stored in Sat
    #note that AOL and RAAN at epoch start are used as opposed to 
    sat_elems = ['Satellite Number', 'Semi-major Axis (km)', 'Eccentricity',\
                 'Inclination (deg)', 'RAAN (deg)', 'Argument of Perigee (deg)',\
                 'Argument of Lattitude (deg)', 'RAAN at Epoch Start (deg)', \
                 'SSP Lat. (deg)', 'SSP Lon. (Deg)', 'Time Since Epoch (sec)', 'dv Used in Current maneuver', 'Dist to Current Target (km)']
    satellites = []
    
    for i in range(num_sats):
        satellites.append([i, 7074, 0, 40, 20*i, 0, 0, -161.155, 0, -161.155, 0, 0,999,999])
    
    #this is the max acceleration available on the satellite
    accel = 0.35*10**(-3)/4 #m/s^2
    
    #Initialize Targets----------------------------------------------------------
    #These are locations of the eye of Typhoon Megi (2010) starting since epoch Oct 10, 2010, 12:00 UTC
    num_targets = 5
    targets = []
    
#    targets_time_days = [2.5, 5, 7.5, 10, 12.5]; #days since epoch
#    targets_time = [element * 3600 *24 for element in targets_time_days] #convert to sec
#    targets_lat = [11.9, 13.2, 17.5, 17.1, 25.0]; #deg
#    targets_long = [141.4, 138.5, 123.6, 117.4, 118.0]; #deg
#    targets = [[targets_time[i], targets_lat[i], targets_long[i]] for i in range(num_targets)]
    targets_time,targets_lat,targets_long, time_since_epoch, latitude, longitude = import_hurricane()
    targets = [[targets_time[i], targets_lat[i], targets_long[i]] for i in range(num_targets)]
    #Time window corresponds to allowed viewing time around each target (ie +/- 20 hrs target time)
    time_window = 20*3600 #sec
    
    
    #Establishes minimum acceptable distance to eye of the storm 
    min_distance_to_eye = 100
    
    
    #Satellite state is stored in dictionary nodes, and in Graph G
    nodeID = 0
    nodes = {0: satellites}
    G = nx.Graph()
    
    #possible dV options (negative dV represents lowering maneuvers, positive dV represents raising maneuvers)
    #dV_min = -dV_max
    #dV_min = -15
   # dV_max = 15
    #dV_step = 0.5
    #dV_list = np.arange(dV_min, dV_max+dV_step, dV_step).tolist()
    #dV_list.remove(0)
    #dV_list
    dV_list = [dV1, dV2, dV3, dV4, dV5]
    
    #propogation time step
    time_step = 10;
    
    
    
    #the node we are starting to pull from
    origin_node = 0
    # the node we are creating
    current_node = 1
    #the information we start with
    old_sat_list = nodes[origin_node].copy()
    calc_nodes_last_target = [0]
    num_target = 0
    
    
    
    calc_nodes_current_target = []
    for target in targets:
        num_target = num_target +1;
        #print('---')
        print("\nExploring options for this target"+"\t")
        print(str(num_target))
        solution_found = False
        
        time_min = target[0] - time_window;        
        time_max = target[0] + time_window;
        time_list = np.arange(time_min, time_max+time_step, time_step)

        lat_interp = np.interp(time_list, time_since_epoch, latitude)
        long_interp = np.interp(time_list, time_since_epoch, longitude)
        current_target = [time_list, lat_interp, long_interp]
        #print(current_target)
        
        new_sat_list = []
        for i in range(num_sats):
            new_sat_list.append([])
        for origin in calc_nodes_last_target:
            #print("List of nodes to branch from", str(calc_nodes_last_target))
            #print("Currently branching from", str(origin))
            old_sat_list = nodes[origin].copy()
            for sat in range(len(old_sat_list)):
                maneuvering_sat = old_sat_list[sat][:]
                duration_min = time_min - maneuvering_sat[10] 
                duration_max = time_max - maneuvering_sat[10]
                duration_list = np.arange(duration_min, duration_max+time_step, time_step)
                 
                #print(duration_min)
                dV = dV_list[num_target-1]
                #for dV in dV_list:
                if dV ==0:
                    flag = 'N/A'
                    updated_sat = propagate(mu, Re, J2, vel_e, rad, flattening, maneuvering_sat, duration_min)
                
                if dV<0:
                    flag = 'LOWER'
                    updated_sat = lowering_maneuver(mu, Re, J2, vel_e, rad, flattening, maneuvering_sat, accel, abs(dV), duration_min)
                    if updated_sat!= None:
                        updated_sat[11] = abs(dV)
                if dV>0:
                    flag = 'RAISE'
                    updated_sat = raising_maneuver(mu, Re, J2, vel_e, rad, flattening, maneuvering_sat, accel, dV, duration_min)
                    if updated_sat!= None:
                        updated_sat[11] = abs(dV)
                    
                    
                if updated_sat !=None: 
                    
                    
                    #now propogate the satellite to the end of the time window to see the number/quality of accesses
                    propagate_sat_options = propagate(mu, Re, J2, vel_e, rad, flattening, updated_sat, (duration_list-duration_min))
                    #print((duration_list-duration_min)/3600.0/24.0)
                    #print(len(propagate_sat_options[8]))
                    
                    
                    #    for i in range(len(lat_interp)):
                    #        print(time_list[i]/3600/24, lat_interp[i], long_interp[i])
                    distance = distance_SSP_to_target(mu, Re, J2, vel_e, rad, flattening,propagate_sat_options ,current_target)
                        
                    num_accesses = 0
                    num_accesses = sum(1 for x in distance if x<min_distance_to_eye )
                    #print('---')
                    #print(num_accesses)
                        
                    if num_accesses>0:
                        #print('The satellite maneuvered with dv:', dV, 'm/s to the following state:')
                        #print(updated_sat)
                        
                        #record all accesses
                        access_distance = []
                        access_time = []
                        index = 0
                        for x in distance:
                            index = index+1
                            if x<min_distance_to_eye:
#                                    print('---')
#                                    print('Target',str(num_target),'successful access')
#                                    #print(x)
                                access_distance.append(x)
                                print(access_distance)
                                access_time.append(time_min+index*time_step)
#                                print('SSP')
                                long = propagate_sat_options[9][index]
#                                print(propagate_sat_options[8][index])
#                                print(long%360)
                                totalSeconds = time_min+index*time_step
                                seconds = int((totalSeconds % 60));
                                minutes = int((totalSeconds % 3600) / 60);
                                hours = int((totalSeconds % 86400) / 3600);
                                days = int((totalSeconds % (86400 * 30)) / 86400);
                                print(datetime.datetime(2010,10,10,12)+ datetime.timedelta(seconds=totalSeconds))
                                print('lat',current_target[1][index])
                                print('long',current_target[2][index])
                                    
                        
                        solution_found = True
                        mean_distance_pass = sum(access_distance)/num_accesses
                        min_distance_pass = min(access_distance)
                        #print(mean_distance_pass)
                        updated_sat[13] = min_distance_pass
                        #updated_sat[13] = mean_distance_pass
                        updated_sat[12] = num_accesses
                        propagate_sat = propagate(mu, Re, J2, vel_e, rad, flattening, updated_sat, time_window*2)
                        new_sat_list[updated_sat[0]] = propagate_sat
                        nodes[current_node] = new_sat_list.copy()
                        propagate_sat =[]
                        updated_sat = []
                        calc_nodes_current_target.append(current_node)
                        if dV ==0:
                            dV_adj = 0.00001 #to ensure graph is connected, for use of dij
                        else:
                            dV_adj = abs(dV)
                            
                        G.add_edge(origin, current_node, dV = dV_adj,dist_to_target = mean_distance_pass,  target_accesses = num_accesses, man_type = flag)
                        #print(current_node)
                        current_node = current_node+1
                    
                        
        if solution_found == False:
            #if a solution cannot be found, propogate sat, and record 0 accesses
            for origin in calc_nodes_last_target: 
                old_sat_list = nodes[origin].copy()
                for x in range(len(old_sat_list)):
                    flag = 'N/A'
                    sat =  old_sat_list[x][:]
                    sat[11]=999
                    sat[12] =999
                    t = 349060
                    duration = t- sat[10]
                    propagate_sat = propagate(mu, Re, J2, vel_e, rad, flattening, sat, duration)
#                    print(propagate_sat[8])
#                    print(propagate_sat[9])
                    if num_target == 2:
                        distance = distance_SSP_to_target(mu, Re, J2, vel_e, rad, flattening,propagate_sat ,[t, 13.2,138.5])
#                    #else:
#                    distance = 999;
#                    new_sat_list[sat[0]] = propagate_sat
                    totalSeconds = t
                    seconds = int((totalSeconds % 60));
                    minutes = int((totalSeconds % 3600) / 60);
                    hours = int((totalSeconds % 86400) / 3600);
                    days = int((totalSeconds % (86400 * 30)) / 86400);
                    #print('target 2---')
                    #print(days,hours,minutes)
                    #print(distance)
                    #print('---')
                    propagate_sat = propagate(mu, Re, J2, vel_e, rad, flattening, sat, duration_max)
                    distance = distance_SSP_to_target(mu, Re, J2, vel_e, rad, flattening,propagate_sat ,target)
                    propagate_sat[13] = distance
                    #propagate_sat[14] = 'N/A'
                    new_sat_list[sat[0]] = propagate_sat.copy()
                    nodes[current_node] = new_sat_list.copy()
                    propagate_sat =[]
                    calc_nodes_current_target.append(current_node)
                    G.add_edge(origin, current_node, target_accesses = 0, dV =0.00001, dist_to_target = distance, man_type = flag)
                    current_node = current_node+1 
        calc_nodes_last_target = calc_nodes_current_target[:]
        calc_nodes_current_target = []
    
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
            shortest_complete_path_length = path_length
    shortest_complete_path_edges = zip(shortest_complete_path,shortest_complete_path[1:])
    shortest_complete_path_edges = set(shortest_complete_path_edges)
    #print(shortest_complete_path_edges)
    
    #record information about the shortest path
    dV_total = 0
    num_accesses_total = 0
    dist_sum = 0
    dist_sum_length=[]
    for i in shortest_complete_path_edges: 
         dV_total = dV_total + G.edges[i]['dV']
         num_accesses_total = num_accesses_total + G.edges[i]['target_accesses']
         
         #print(G.edges[i]['dist_to_target'])
         if G.edges[i]['dist_to_target']< min_distance_to_eye:
            dist_sum_length.append(G.edges[i]['dist_to_target'])
    if len(dist_sum_length)>0:
        dist_mean = sum(dist_sum_length)/len(dist_sum_length)
    else:
        dist_mean= 99999
    
    return [dV_total, -num_accesses_total, dist_mean]


#G and nodes contains all information about the generated tree. 
#dV, accesses, dist contains information about the lowest dV path

#import matplotlib.pyplot as plt
#from timeit import default_timer as timer
#import networkx as nx
#import csv
#try:
#   import pygraphviz
#   from nx.drawing.nx_agraph import graphviz_layout
#except ImportError:
#   try:
#       import pydot
#       from networkx.drawing.nx_pydot import graphviz_layout
#   except ImportError:
#       raise ImportError("This example needs Graphviz and either "
#                         "PyGraphviz or pydot")
#
#start = timer()
#[dV, accesses, dist, G, nodes, shortest_complete_path, shortest_complete_path_edges] = tree_generation5(-0.5,0,-0.5,0.5,0.5)
#end = timer()
#elapsed_time = end-start
#print(elapsed_time)
[dV, accesses, dist] = series_of_maneuvers(0,0,0,0,0)
#[dV, accesses, dist] = tree_generation5(-1.53	,6.17,	-0.12,	0.1,0.15)
#1.90001 -7 82.5493850201865
#[dV, accesses, dist] = tree_generation5(-1.43	,6.07,	-0.02,	0,0.25)
#1.70002 -9 88.44367017474661
#[dV, accesses, dist] = tree_generation5(-1.33	,5.97,	0,	-0.1,0.05)
#1.4800200000000003 -7 84.57861883401051

#print(dV, accesses, dist)
#
#
#w = csv.writer(open("output_4_16_2021_15ms_manresult_80.csv", "w"))
#for key, val in nodes.items():
#    w.writerow([key, val])
#
##generate a visuzalition of the graph
#pos = graphviz_layout(G, prog='twopi')
#plt.figure(figsize=(100, 100))
#nx.draw(G, pos, node_size=200, alpha=0.5, node_color="grey", with_labels=True)
##rounded edge labels from https://stackoverflow.com/questions/60397606/how-to-round-off-values-corresponding-to-edge-labels-in-a-networkx-graph
#edge_labels = dict([((u,v,), f"{d['dV']:.2f} m/s, {d['dist_to_target']:.2f}, {d['target_accesses']:.2f} accesses") for u,v,d in G.edges(data=True)]) 
##edge_labels = dict([((u,v,), f"{d['dV']:.1f}") for u,v,d in G.edges(data=True)]) 
#nx.draw_networkx_edge_labels(G, pos, edge_labels= edge_labels)
#
#for i in shortest_complete_path_edges:
#    print(i)
#    print(edge_labels[i])
#
#nx.draw_networkx_nodes(G,pos,nodelist=shortest_complete_path,node_color='r')
#nx.draw_networkx_edges(G,pos,edgelist=shortest_complete_path_edges,edge_color='r',width=5)
#plt.axis('equal')
#plt.savefig('test_tree_4_16_2021_GA_manresult_80.png')

