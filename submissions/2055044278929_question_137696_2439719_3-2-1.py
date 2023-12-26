# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:14:59 2023

@author: Administrator
"""

import random
n=random.randint(5,10)
for i in range(n):
    s=chr(97+i)
    print(" "*(9-i),s*(2*i+1))


    