import math
def solve(a,b):
    n=2500001
    sieve=[1]*n
    sieve[0]=0
    sieve[1]=0
    m=int(math.sqrt(n))
    for i in range(2,m+1):
        if sieve[i]==1:
            for j in range(i*i,n,i):
                sieve[j]=0
    c=0
    for i in range(a,b+1):
        if sieve[i]==1 and sieve[i+2]==1 and b-i>=2:
            c=c+1
    return c
start,end=map(int,input().split())
print(solve(start,end))
