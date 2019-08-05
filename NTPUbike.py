# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:39:51 2019

@author: ASUS
"""

import requests
import json


class NTPUbike():
    def __init__ (self):
        self.content = ''
        
        self.response = json.loads(requests.get("http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json").text)






    def getBike(self):
        self.area = ''
        for row in self.response:
            if row ['sarea'] not in self.area:
            #if not (row ['sarea'] in self.area):
                self.area += row['sarea'] + ' '
        return self.area
    
    def getAreaBike(self,area):
        self.bike = ''
        for row in self.response:
            if row['sarea'] == area:
                self.bike += row['sna'] + ' ' + row['sbi'] + ' ' + row['bemp'] + '\n' 
                
        return self.bike
    
    
#tp =  NTPUbike()
#print(tp.getBike()) 
#print(tp.getAreaBike('三重區'))      
        



