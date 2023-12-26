import math
pi=2
for n in range(2,1001):
    pi=pi*(n**2)/((n-1)*(n+1))
    n=n+2
a=float(math.pi)
b=abs(math.pi-pi)
print("n=1000时π的近似值为%f"%pi,'π的值为:',a,'误差为:',b)
