n = int(input())
l = list(map(int,input().split()))
s = []
z = []
for i in range (n):
    if l[i]%2==0:
        z.append(l[i])
    else:
        s.append(l[i])
t = z+s
print(t)
