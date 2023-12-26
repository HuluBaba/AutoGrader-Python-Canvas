a=int(input("请输入a（a为1-9）: "))
n=int(input("请输入n（n为5-10）: "))
Sn=0
temp=0
print("s=",end="")
for i in range(1,n):
         temp=temp*10+a
         Sn+=temp
         print(temp,"+",end="")
b=str(temp)+str(a)
Sn=int(b)+Sn
print(b,"=",Sn)