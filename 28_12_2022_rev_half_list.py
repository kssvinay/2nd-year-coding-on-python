n = int(input())
l = list(map(int,input().split()))
s = []
for i in range(len(l)):
  if i<len(l)//2:
    s+=[l[i]]
  else:
    s+=[len(l)-l[i]]
