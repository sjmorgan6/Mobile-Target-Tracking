import math
import numpy as np

def distance_SSP_to_target(mu, Re, J2, vel_e, rad, flattening, sat, target):
# expects sat.SSP_lat/long and target.lat/long in degrees
# result is in km
    
    SSP_lat = sat[8]
    SSP_long = sat[9]
    
    target_lat = target[1]
    target_long = target[2]
    
    
    distance = 2.0*Re*\
    np.arcsin(np.sqrt((np.sin((SSP_lat*rad-target_lat*rad)/2.0))**2.0+\
    np.cos(SSP_lat*rad)*np.cos(target_lat*rad)*(np.sin((SSP_long*rad-target_long*rad)/2.0))**2.0))/\
    1000.0;
    return distance