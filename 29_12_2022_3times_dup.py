n = int(input())
l = list(map(int,input().split()))
k = []
for i in l:
  if l.count(i) != 3:
    k+=[i]
