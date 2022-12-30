n = list(map(int,input().split()))
l = list(map(int,input().split()))
c = n[0]
d = n[1]
k=[]
for i in range(d,c):
  k+=[i]
for i in range(d):
  k+=[i]
print(k)
