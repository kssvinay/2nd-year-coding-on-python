'''assignment1:
    write a program to convert string into following format

    for example:
        aaabb
    output:
        3a2b'''
s = k = input()
ans = ''
for i in s:
    if i not in ans:
        ans+=str(s.count(i))+i
        s = s.replace(i,'')
print(ans)
