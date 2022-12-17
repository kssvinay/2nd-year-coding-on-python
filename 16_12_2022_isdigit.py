s = input()
n = len(s)
cnt=0
for i in range(n):
    if s[i].isdigit()==1:
        cnt+=1
print(cnt)
