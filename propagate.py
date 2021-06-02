#---------------------------------------------
# Written by Sarah Morgan (sjmorgan@mit.edu, sjmorgan162@gmail.com)
# This code is a result of my (Sarah Morgan's) SM thesis here: [[3]](#3). Several case studies are shown there with a more in-depth discussion of this procedure of adaptable maneuver planning. 
# © Massachusetts Institute of Technology 2021.
# RAAN_AOL_equations_python sourced from: DOI: https://doi.org/10.5281/zenodo.4452978 These are from the paper: https://doi.org/10.2514/1.G003739
#----------------------------------------------- 
def propagate(mu, Re, J2, vel_e, rad, flattening, sat, accel, duration):

    import numpy as np
    from RAAN_AOL_equations_python import full_man_low
    
    tmaneuver = duration #sec
    deltaVtotal = 0 #m/s
    a0 = sat[1] #m
    a3 = sat[1] #m
    incl = sat[2]*rad #rad
    RAAN0 = sat[3]*rad #rad
    u0 = sat[4]*rad #rad
    RA_epoch = sat[5]*rad #rad
    
    new_sat = sat[:]
    
    
    #Use McGrath's equations to find new RAAN and u post-maneuver:
    #this is from 
    #note these inputs should be in meters, seconds, and radians
    [RAANtotal_low, utotal_low] = full_man_low(mu, Re, J2, RAAN0, u0, accel, a0, a3, incl, deltaVtotal, tmaneuver)
    
    
    #Update the satellite states and find the new subsatellite point
    #update satellite time
    new_sat[8] = sat[8]+ tmaneuver;  
    
    #lat SSP geocentric
    lat_SSPc = np.arcsin(np.sin(incl)*np.sin(utotal_low)); #this is geocentric
    
    #lat_SSP geodetic
    new_sat[6] = (np.arctan(np.tan(lat_SSPc)/(1 - flattening * (2 - flattening))))/rad;  
    
    #long_SSP
    new_sat[7] = (np.arctan2(np.cos(incl)*np.sin(utotal_low),np.cos(utotal_low))\
        -vel_e*(new_sat[8])+RAANtotal_low-RA_epoch)/rad;
    
    #RAAN       
    new_sat[3] = RAANtotal_low/rad;
    #AoL
    new_sat[4] = utotal_low/rad;

    #record dV used
    new_sat[9] = deltaVtotal
    
    return new_sat