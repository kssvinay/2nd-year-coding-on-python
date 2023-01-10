s=list(map(int,input()))
s.sort(reverse=True)
res=''
for i in s:
    res=res+str(i)
print(res)
