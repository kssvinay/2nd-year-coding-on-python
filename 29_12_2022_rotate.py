n = list(map(int,input().split()))
l = list(map(int,input().split()))
c = n[0]
d = n[1]
k=[]
for i in range(d,c):
  k+=[a[i]]
for i in range(d):
  k+=[a[i]]
print(k)
