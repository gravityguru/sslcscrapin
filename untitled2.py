#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:50:53 2019

@author: vins
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup as bs
import requests;
u= 20190800001

while u>20190070001:
    u=u-1
    try:
        r = requests.post('http://karresults.nic.in/ressslc2019.asp', data = {'InputRegno':u})
        s=bs(r.content,'lxml')
        for t in s.find_all('td'):
            print(t.string)
            st=str(t.string)
            st=st+"\n"
            
            with open('resultfinalvs123.txt','a') as xlsfile:
                xlsfile.write(st)
    except:
        print("An exception occurred")
    

    
