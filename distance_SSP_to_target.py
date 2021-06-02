import numpy as np

def distance_SSP_to_target(mu, Re, rad, SSP_lat, SSP_long, target_lat, target_long):
# expects sat SSP_lat/long and target lat/long in degrees
# Uses Haversine distance formula
# result is in m
    
    distance = 2.0*Re*\
    np.arcsin(np.sqrt((np.sin((SSP_lat*rad-target_lat*rad)/2.0))**2.0+\
    np.cos(SSP_lat*rad)*np.cos(target_lat*rad)*(np.sin((SSP_long*rad-target_long*rad)/2.0))**2.0));
    return distance