n = int(input())
m = []
c = 0
for i in range(0, n):
    l = []
    for j in range(0, n):
        x = float(input())
        l.append(x)
    m.append(l)
for i in range(0, n):  
    sum = 0
    for j in range(0, n):  
        sum = sum + m[i][j]
    if sum == 2:
        c = c + 2
for i in m:
    print(i)
if c == 6:
    print('Coder target matrix')
else:
    print('Not a coder target matrix')
