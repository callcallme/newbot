# -*- coding: utf-8 -*-
"""
Created on Fri May 25 20:41:10 2018

@author: ASUS
"""

import requests
import json

def getBike():
    response = json.loads(requests.get("http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json").text)
    
    
        
    station = [];
    sbi = []
    bemp = []
    
    for stat in response:
        station.append(stat['sna'])
        sbi.append(stat['sbi'])
        bemp.append(stat['bemp'])
    
    content = ''
    for i in range(5):
        content += station[i] +'-' + sbi[i] +'-' + bemp[i] + '\n'
        
    return content
    

    
    
    
    







    