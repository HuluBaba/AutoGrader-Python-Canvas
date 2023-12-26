# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:18:34 2023

@author: Administrator
"""

import random
n=random.randint(90,100)            
if n % 2 !=0:    #奇数情况
    for i in range(1,int((n+1)/2+1)):
        z=64+i
        Z=chr(z)
        enter=int((n+1)/2)
        print ("{}{}".format((enter-i)*" ",(2*i-1)*Z))
    for i in range(enter+1,n+1):
        z=64+i
        Z=chr(z)
        enter=int((n+1)/2)
        print ("{}{}".format((i-enter)*" ",(-2*(i-enter)+n)*Z))
elif n % 2 ==0:        #偶数情况
    for i in range(1,int((n+1)/2+1)):
        z=64+i
        Z=chr(z)
        enter=int((n+1)/2)
        print ("{}{}".format((enter-i)*" ",(2*i-1)*Z))
    for i in range(enter+1,n+1):
        z=64+i
        Z=chr(z)
        enter=int((n+1)/2)
        print ("{}{}".format((i-enter-1)*" ",(-2*(i-enter)+n+1)*Z))