import math
n=2500001
sieve=[1]*n#filling 1 value from 0 to n-1 in sieve list
sieve[0]=0
sieve[1]=0
m=int(math.sqrt(n))
for i in range(2,m+1):
    if sieve[i]==1:
        for j in range(i*i,n,i):#factors of i will fill with 0
            sieve[j]=0
start,end=map(int,input().split())
s=''
for i in range(start,end+1):#(inclusive first and last values)
    if sieve[i]==1:
        s=s+str(i)
print(len(s) )
