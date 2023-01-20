'''assignment2:
    write a program to print missing character ascii code
    for example
    input:abd
    ouput:99'''
def asc(e):
    return ord(e)
s = list(input())
s.sort(key = asc)
j = ord(s[0])
for i in s:
    if ord(i) == j:
        j+=1
    else:
        print(j)
        break
