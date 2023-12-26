import random
n=random.randint(5,10)
i=0
for asc in range(97,n+97):
    i=i+1
    print(' '*(n-i),chr(asc)*(2*i-1))