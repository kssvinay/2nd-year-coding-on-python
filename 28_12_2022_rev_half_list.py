count = int(input())
given = list(map(int,input().split()))
first = []
remain=[]
for i in range(len(given)):
    if i<len(given)//2:
        first+=[given[i]]
    else:
        remain+=[given[i]]
print(first+remain[::-1])
