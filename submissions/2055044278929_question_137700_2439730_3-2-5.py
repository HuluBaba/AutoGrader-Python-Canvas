# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:27:07 2023

@author: Administrator
"""

x=int(input("请输入一个正整数："))
fx=0
while x>0:#循环条件
    d=x%10#取得倒数第一位
    x=x//10#取得前几位
    fx=fx*10+d#数学思维，不是很好想，不断循环
print("反序数为：",fx)
    