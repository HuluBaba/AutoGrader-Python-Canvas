# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:49:28 2023

@author: lenovo
"""
a = eval(input("请输入一个数字(1~9)："))
n = eval(input("请输入次数n(5~10)："))
sum = []
s1 = 0
i = 0
s=0
for i in range(0,n):
    s1 = s1+(a*(10**i))
    s=s+s1
    sum.append(s1)
    i += 1
sum1 = [str(i) for i in sum]
print("s=","+".join(sum1),"=",s)
	
    
	
	


