import math
m=10000001
sieve=[1]*m
sieve[0]=sieve[1]=0
x=int(math.sqrt(m))
for i in range(2,x+1):
        if sieve[i]==1:
                for j in range(i*i,m,i):
                        sieve[j]=0
pf=[0]*m
for i in range(2,m):
        if sieve[i]==1:
                pf[i]=pf[i-1]+1
        else:
                pf[i]=pf[i-1]
t=int(input())
for i in range(t):
        n=int(input())
        print(pf[n])
