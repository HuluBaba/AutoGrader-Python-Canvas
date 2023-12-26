# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:18:13 2023

@author: lenovo
"""

n=0
for x in range(1,5):
    for y in range(x+1,6):
        for z in range(5,7):
            if y<z:
                print("%d %d %d"%(x,y,z))
                n=n+1
print("共有%d种排法"%n)
