a=int(input('请输入任意位正整数x='))
c=0
while (a//10)!=0:
    b=a%10
    c=c*10+b
    a=a//10
c=c*10+a
print('逆序数为%d'%c)