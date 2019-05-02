#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:45:43 2019

@author: luhao
"""

import geocoder_tool
import numpy as np
import pandas as pd


gll = geocoder_tool.get_latlng_list
cl = geocoder_tool.code_list_cleanup
code_list = []
print('Input JSON name (first capital): ')
x = input()
json_path = '/Users/luhao/Desktop/Project/Scraped_results/' + x + '.json'

code_list = cl(gll(json_path, code_list))

code_array = np.array(code_list)
code_df = pd.DataFrame({'Lat': code_array[:,0], 'Lon': code_array[:,1]})
code_df.to_csv('/Users/luhao/Desktop/Project/Geocoder_tool/Geocodes/%s.txt' % x, index=None)



