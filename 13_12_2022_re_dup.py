l=[1,2,3,2,3,4,5,6]
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)
