# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 05:03:57 2020

@author: 17035
"""
def import_hurricane():
    # import hurricane track data
    import pandas as pd
    import datetime
    
    data = pd.read_excel(r'C:\Users\17035\Documents\2020_ReCon\SMorgan_TreeGenerationStandaloneModel_Python\hurricane_data.xlsx')
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
    date_epoch = datetime.datetime(2010,10,10,12)
    for i in range(len(date_time)):
            time_delta = (date_time[i]-date_epoch)
            time_since_epoch.append(time_delta.total_seconds())
    
    target_time = []
    target_lat = []
    target_long = []
    
    #num_targets = 5
    #time_interval = 2.5*24*3600 #2.5days
    
    num_targets = 5
    time_interval = 2.5*24*3600 #2.5days
    for i in range(num_targets):
        index = time_since_epoch.index((i+1)*time_interval)#+2.5*24*3600)
        target_time.append(time_since_epoch[index])
        target_lat.append(latitude[index])
        target_long.append(longitude[index])
    
    return target_time,target_lat,target_long, time_since_epoch, latitude, longitude

