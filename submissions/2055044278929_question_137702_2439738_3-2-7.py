# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:28:57 2023

@author: Administrator
"""

p=2
n=1
while n<=1000:
    p=p*(n*2)**2/((2*n-1)*(2*n+1))
    n+=1
print("pi的近似值为：",p)
import math
print("\n",math.pi)
