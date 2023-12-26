# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:37:00 2023

@author: lenovo
"""

import random
n=random.randint(1,101)
a=eval(input("请输入猜测的数："))
i=1
while a!=n:
    if a>n:
        print("大了")
    elif a<n:
        print("小了")
    i=i+1
    a=eval(input("请输入猜测的数："))
if a==n:
    print(n,"恭喜你猜对了！你猜了%d次"%i)