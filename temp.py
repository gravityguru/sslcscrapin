# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup as bs
import requests;
u=20190070001

while u<20190800001:
    try:
        r = requests.post('http://karresults.nic.in/ressslc2019.asp', data = {'InputRegno':20190800001})
        s=bs(r.content,'lxml')
        for t in s.find_all('td'):
            print(t.string)
            st=str(t.string)
            st=st+"\n"
            u++
            with open('result1.txt','a') as xlsfile:
                xlsfile.write(st)
    except:
        print("An exception occurred")