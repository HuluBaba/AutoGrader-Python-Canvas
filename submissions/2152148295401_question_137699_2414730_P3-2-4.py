str=input('输入的字符句子：')
ls=list(str.split())
max=ls[1]
for i in ls:
    if(len(max)<len(i)):
        max=i
print('最长的单词为%s'%max)
    