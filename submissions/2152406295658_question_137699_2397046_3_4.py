# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:37:01 2023

@author: lenovo
"""

s=input("请输入一个英语句子：")
words=s.split(" ")
max=words[-1]
for word in words[-1::-1]:
    if len(word)>len(max):
        max=word
print(max)