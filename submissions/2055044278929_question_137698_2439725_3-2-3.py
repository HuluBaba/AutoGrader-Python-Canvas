# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:25:32 2023

@author: Administrator
"""

x=str(input("请输入一个表达式："))
n左=0
n右=0
for i in range(len(x)):
    if x[i]=="(":
        n左+=1
    if x[i]==")":
        n右+=1
print("有",n左,"个左括号","有",n右,"个右括号")
    
