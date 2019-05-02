import geocoder
import json
from interval import Interval
import re



def get_latlng_list(json_path, code_list):
    with open(json_path, encoding='utf-8') as f:
        file = json.loads(f.read()) 
    if 'Monster' in re.findall(r'[\w]+', json_path):
        for i in file:
            code_list.append(geocoder.arcgis(i['postcode']).latlng)
    else:    
        for i in file:
            code_list.append(geocoder.arcgis(i['location']).latlng)                             
    return code_list

def code_list_cleanup(code_list):
    lat_interval = Interval(49.87, 61.02)
    lon_interval = Interval(-8.25, 1.83)
    newlist = []
    for latlng in code_list:
        if latlng != None and latlng[0] in lat_interval and latlng[1] in lon_interval:
            newlist.append(latlng)
    return newlist
    
