n=1
sum=0
i=1
while(1/n>=10**(-4)):
    sum=sum+1/n
    n=n+i
    i=i+1
print("S=1+1/2+1/4+1/7+1/11+1/16+1/22+1/29+...=%f"%sum)