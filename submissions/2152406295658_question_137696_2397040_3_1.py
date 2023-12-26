# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:35:29 2023

@author: lenovo
"""

import random
n=random.randint(5,11)
ch='a'
for i in range(1,n+1):
    print(" "*(n+3-i),ch*(2*i-1))
    ch=chr(ord(ch)+1)