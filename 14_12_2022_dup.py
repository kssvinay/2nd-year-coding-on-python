n=int(input())
l=[]
for i in range(1,n+1):
    num=int(input())
    l.append(num)
dup=[]
for i in l:
    if(i not in dup):
        dup.append(i)
print(dup)
if(dup==l):
    print('yes')
else:
    print('no')
