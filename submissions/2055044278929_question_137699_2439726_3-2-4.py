# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:26:33 2023

@author: Administrator
"""

stra=input("请输入一个英文句子:")
li=stra.split(" ")#利用split方法，将单词分离到列表中
print(li)
max_length=0#便于计数
longest_stra=""
for i in li:#遍历列表
    if len(i)>max_length:#开始比较并计数
        max_length=len(i)
        longest_stra=i#找到最长单词
print("最长单词是：",i)