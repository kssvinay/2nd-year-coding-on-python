n = int(input())
l = list(map(int,input().split()))
k = int(input())
c=0
for i in range (n):
    for j in range(i+1,n):
        if l[i] - l[j]==k:
            c=c+1
if c==0:
    print('no')
else:
    print('yes')
