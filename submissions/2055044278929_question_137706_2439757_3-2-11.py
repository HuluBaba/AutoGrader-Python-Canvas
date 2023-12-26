# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:35:30 2023

@author: Administrator
"""

import random
s=random.randint(1,100)
n=1
cc=eval(input("请输入你猜的数："))
while s!=cc:
     if cc<s:
        print("猜小了")
     else:
        print("猜大了")
     cc=eval(input("猜错了，再猜一次："))
     n+=1
else:
    print("恭喜你，猜对了！")
    print("猜了",n,"次")
    