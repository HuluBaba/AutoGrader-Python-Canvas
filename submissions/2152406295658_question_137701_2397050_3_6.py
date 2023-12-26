# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:14:11 2023

@author: lenovo
"""

s=0
t=1
i=1
while t<=10000:
    s=s+1/t
    t=t+i  
    i=i+1
print(s)