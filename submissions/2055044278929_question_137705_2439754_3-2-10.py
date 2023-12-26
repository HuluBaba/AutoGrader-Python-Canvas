# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:34:52 2023

@author: Administrator
"""

i=0
for x in range(1,7):
    for y in range(x+1,7):
        for z in range(y+1,7):
            if z>=5:
                i+=1
                print("\nx在周",x,"考","y在周",y,"考","z在周",z,"考")
print("共有",i,"种方案")