n = int(input())
l = list(map(int,input().split()))
s = int(input())
for i in range(len(l)) :
    if l[i]==s:
        print(i)
