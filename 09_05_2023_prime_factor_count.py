import math
n=int(input())
c=0
while(n%2==0):
    c=c+1
    n=n//2
for i in range(3,int(math.sqrt(n))+1,2):
    while(n%i==0):
        c=c+1
        n=n//i
if n>2:
    c=c+1
print(c)
