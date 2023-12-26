import random
x=random.randint(1,100)
print("猜数游戏")
n=0
while 1:
    n=n+1
    a=int(input("输入猜测的数："))
    if(a<x):
        print("%s 小了"%a)
    elif(a>x):
        print("%s 大了"%a)
    else:
        break
print("%s 恭喜你猜对了！你猜了%s次"%(x,n))
