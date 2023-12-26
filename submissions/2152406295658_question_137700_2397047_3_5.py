# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:51:59 2023

@author: lenovo
"""

s=input("请输入一个正整数：")
x=int(s)
for i in range(0,len(s)):
    y=x%10
    x=x//10
    print(y,end="")