#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:07:11 2019

@author: luhao
"""

import geocoder
import pandas as pd
import numpy as np

postcode = pd.read_csv('/Users/luhao/Desktop/Geocoder_tool/Registered_Landfills.csv', usecols=[8])
postcode_list = np.array(postcode['SitePostCode'].tolist()).tolist()
poco = [x.replace('nan', 'NA') for x in postcode_list]

location = pd.read_csv('/Users/luhao/Desktop/Geocoder_tool/Registered_Landfills.csv', usecols=[2,3,4,5,6,7])
location_array = np.array(location.values.tolist())
loc_list = [','.join(x) for x in location_array]
loc = [x.replace('nan,', '') for x in loc_list]
    
regi_code = []
for i in range(0, 564):
    if poco[i] != 'NA':
        if geocoder.arcgis(poco[i]).latlng != None:
            geocode = geocoder.arcgis(poco[i]).latlng
        print('Done +1 using poco')
    else:
        geocode = geocoder.arcgis(loc[i]).latlng
        print('Done +1 using loc')
    if geocode != None:
        regi_code.append(geocode)
        print('-------Success +1--------')
regi_array = np.array(regi_code)
regi_df = pd.DataFrame({'Lat': regi_array[:,0], 'Lon': regi_array[:,1]})
regi_df.to_csv('regi_code.txt', index=None)
    