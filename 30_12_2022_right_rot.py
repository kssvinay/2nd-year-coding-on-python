n = list(map(int,input().split()))
l = list(map(int,input().split()))
a = l[:n[0]-n[1]]
b = l[n[0]-n[1]:]
for i in b+a:
    print(i,end=" ")
