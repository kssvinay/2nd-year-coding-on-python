n = int(input())
m=[]
ld=rd=0
for i in range(n):
    l =[]
    for j in range (n):
        x = int(input())
        l.append(x)
    m.append(l)
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            ld=ld+m[i][j]
        if i==j:
            rd=rd+m[i][j]
print(ld-rd)
