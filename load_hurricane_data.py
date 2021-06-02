# -*- coding: utf-8 -*-
#---------------------------------------------
# Written by Sarah Morgan (sjmorgan@mit.edu, sjmorgan162@gmail.com)
# This code is a result of my (Sarah Morgan's) SM thesis here: [[3]](#3). Several case studies are shown there with a more in-depth discussion of this procedure of adaptable maneuver planning. 
# © Massachusetts Institute of Technology 2021.
#----------------------------------------------- 
def import_hurricane(file, date_epoch, num_targets, time_interval):
    # import hurricane track data
    import pandas as pd
    import datetime
    
    #Mobile track file is organized as an Excel file with 6 columns = Year/ Month/ Day/ Hour/ Latitude (deg) / Longitude (deg) (time presumed UTC)
    data = pd.read_excel(file)
    year = data['Year'].tolist()
    month = data['Month'].tolist()
    day = data['Day'].tolist()
    hour = data['Hour'].tolist()
    latitude = data['Lat.'].tolist()
    longitude =  data['Long.'].tolist()
    
    date_time = []
    for i in range(len(year)):
        date_time.append(datetime.datetime(year[i], month[i], day[i], hour[i]))
    
    time_since_epoch = []
    for i in range(len(date_time)):
            time_delta = (date_time[i]-date_epoch)
            time_since_epoch.append(time_delta.total_seconds())
    
    target_time = []
    target_lat = []
    target_long = []
    
    for i in range(num_targets):
        index = time_since_epoch.index((i+1)*time_interval)
        target_time.append(time_since_epoch[index])
        target_lat.append(latitude[index])
        target_long.append(longitude[index])
    
    return target_time,target_lat,target_long, time_since_epoch, latitude, longitude

