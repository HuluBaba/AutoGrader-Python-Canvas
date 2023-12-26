# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:32:43 2023

@author: Administrator
"""

s=t=i=1
while 1/t>=1e-4:#循环条件
    t=t+i#找规律，分母的表达
    i+=1#i递增
    s+=1/t#累加s
print("级数的值为：",s)