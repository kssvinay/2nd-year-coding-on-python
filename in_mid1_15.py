#Assignment-15:
#Write a program to print Unique single number for the duplicate list?

l = list(map(int,input().split()))
ul = []
for i in l:
    if i not in ul:
        ul.append(i)
print(ul)
