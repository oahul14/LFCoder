#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:18:30 2019

@author: luhao
"""


import pandas as pd
import numpy as np
from interval import Interval


gl_border = {"minlon": -0.511482, "minlat": 51.28554, "maxlon": 0.335437, "maxlat": 51.69344}
wm_border = {"minlon": -2.208211, "minlat": 52.3457, "maxlon": -1.422524, "maxlat": 52.6643}
gm_border = {"minlon": -2.732097, "minlat": 53.32613, "maxlon": -1.90804, "maxlat": 53.68742}

wmlist = []
gmlist = []
gllist = []
gmaulist = []
glaulist = []
wmaulist = []

gllat = Interval(gl_border['minlat'], gl_border['maxlat'])
gllon = Interval(gl_border['minlon'], gl_border['maxlon'])
wmlat = Interval(wm_border['minlat'], wm_border['maxlat'])
wmlon = Interval(wm_border['minlon'], wm_border['maxlon'])
gmlat = Interval(gm_border['minlat'], gm_border['maxlat'])
gmlon = Interval(gm_border['minlon'], gm_border['maxlon'])

reed = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/reed13456.txt').values.tolist()
cv = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/cv13456.txt').values.tolist()
indeed = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/indeed13456.txt').values.tolist()
monster = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/monster13456.txt').values.tolist()
total = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/total13456.txt').values.tolist()
independent = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/independent13456.txt').values.tolist()
glass = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/glass13456.txt').values.tolist()
au = pd.read_csv('/Users/luhao/Desktop/Project/Geocoder_tool/regi_code.txt').values.tolist()

sumlist = reed+cv+indeed+monster+total+independent+glass

for latlng in sumlist:
    if latlng[0] in gllat and latlng[1] in gllon:
        gllist.append(latlng)
gl_array = np.array(gllist)
gl_df = pd.DataFrame({'Lat': gl_array[:,0], 'Lon': gl_array[:,1]})
gl_df.to_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/GLon.txt', index=None)

for latlng in sumlist:
    if latlng[0] in wmlat and latlng[1] in wmlon:
        wmlist.append(latlng)
wm_array = np.array(wmlist)
wm_df = pd.DataFrame({'Lat': wm_array[:,0], 'Lon': wm_array[:,1]})
wm_df.to_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/WMid.txt', index=None)
   
for latlng in sumlist:
    if latlng[0] in gmlat and latlng[1] in gmlon:
        gmlist.append(latlng)
gm_array = np.array(gmlist)
gm_df = pd.DataFrame({'Lat': gm_array[:,0], 'Lon': gm_array[:,1]})
gm_df.to_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/GMan.txt', index=None)

for latlng in au:
    if latlng[0] in gllat and latlng[1] in gllon:
        glaulist.append(latlng)
glau_array = np.array(glaulist)
glau_df = pd.DataFrame({'Lat': glau_array[:,0], 'Lon': glau_array[:,1]})
glau_df.to_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/GLon_AU.txt', index=None)

for latlng in au:
    if latlng[0] in wmlat and latlng[1] in wmlon:
        wmaulist.append(latlng)
wmau_array = np.array(wmaulist)
wmau_df = pd.DataFrame({'Lat': wmau_array[:,0], 'Lon': wmau_array[:,1]})
wmau_df.to_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/WMid_AU.txt', index=None)

for latlng in au:
    if latlng[0] in gmlat and latlng[1] in gmlon:
        gmaulist.append(latlng)
gmau_array = np.array(gmaulist)
gmau_df = pd.DataFrame({'Lat': gmau_array[:,0], 'Lon': gmau_array[:,1]})
gmau_df.to_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/GMan_AU.txt', index=None)
