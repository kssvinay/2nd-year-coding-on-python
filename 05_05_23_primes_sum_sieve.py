seive=[]
n=int(input())
n=n+1
for i in range(0,n):
    seive.append(1)
for i in range(2,int(n**(0.5))+1):
    if seive[i]==1:
        for j in range(i*i,n,i):
            seive[j]=0
sum = 0
for i in range(2,n):
    if seive[i]==1:
        sum += i
print(sum,end=' ')
