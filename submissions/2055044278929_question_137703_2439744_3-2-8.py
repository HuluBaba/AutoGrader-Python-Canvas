# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:33:20 2023

@author: Administrator
"""

#法一
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
                s=a**3+b**3+c**3
                if s==a*100+b*10+c and s>=100:#注意判断是三位数
                   print("所有的水仙花数为：",s)
#法二
for i in range(100,1000):
    s=(i%10)**3+(i//10%10)**3+(i//100)**3
    if i==s:
        print("水仙花数：",i)
