# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:20:21 2023

@author: lenovo
"""

str=input("请输入一个算术表达式：")
left=0
right=0
for i in str:
    if i == "(":
        left += 1
    elif i == ")":
        right += 1
if left==right:
    print("配对成功")
elif left>right:
    print("左括号多于右括号")
elif left<right:
    print("右括号多于左括号")
    
    

