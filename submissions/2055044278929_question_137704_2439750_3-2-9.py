# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:34:07 2023

@author: Administrator
"""

a=eval(input("请输入a(0~9)："))
n=eval(input("请输入n（5~10）："))#按题目要求输出数字
temp=s=0
stra=""
for i in range(1,n+1):
         temp=temp*10+a#找规律
         s+=temp#累加计算结果
         stra+=str(temp)+"+"#字符串循环
print("s={}={}".format(stra.rstrip("+"),s))#rstrip函数用于删除字符串最后一位