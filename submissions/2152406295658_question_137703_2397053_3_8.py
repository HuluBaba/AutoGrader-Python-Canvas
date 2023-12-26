# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:23:37 2023

@author: lenovo
"""

for n in range(100,1000):
    a=n%10
    b=n//10%10
    c=n//100%10
    if n==a**3+b**3+c**3:
        print(n)
