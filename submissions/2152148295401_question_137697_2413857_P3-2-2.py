import random
n=random.randint(5,10)
i=0
a=0
if n%2!=0:
    b=int((n+1)/2)
    for asc in range(65,b+65):
        i=i+1
        print(' '*(b-i),chr(asc)*(2*i-1))
    for asc in range(b+65,n+65):
        a=a+1
        print(' '*a,chr(asc)*(n-2*a))   
            
            
else:
    c=int(n/2)
    for asc in range(65,c+65):
        i=i+1
        print(' '*(c-i),chr(asc)*(2*i-1))
    for asc in range(c+65,n+65):
        a=a+1
        print(' '*(a-1),chr(asc)*(n-2*a+1))    