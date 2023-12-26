# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:46:25 2023

@author: lenovo
"""
pi=2
for n in range(1,1001):
    pi=pi*((2*n)**2)/((2*n-1)*(2*n+1))
    n=n+1
print(pi)
