n = int(input())
m=[]
for i in range(n):
    l =[]
    for j in range (n):
        x = int(input())
        l.append(x)
    m.append(l)
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(m[i][j])
