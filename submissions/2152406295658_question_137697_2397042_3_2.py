# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:36:23 2023

@author: lenovo
"""
import random
n=random.randint(5,11)
ch='A'
if (n%2)!=0:
    for i in range(1,(n+1)//2+1):
        print(" "*(((n+1)//2)-i),ch*(2*i-1))
        ch=chr(ord(ch)+1)
    for i in range((n+1)//2+1,n+1):
        print(" "*(i-(n+1)//2),ch*(2*(n-i)+1))
        ch=chr(ord(ch)+1)
if (n%2)==0:
    for i in range(1,n//2+1):
        print(" "*(n//2-i),ch*(2*i-1))   
        ch=chr(ord(ch)+1)
    for i in range(n//2+1,n+1):
        print(" "*(i-n//2-1),ch*(2*(n-i)+1))
        ch=chr(ord(ch)+1)

