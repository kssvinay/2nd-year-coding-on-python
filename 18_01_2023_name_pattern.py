'''
Write a program to print your name like this
Name:Teja
Output:
T
TE
TEJ
TEJA
'''
name = input()
for i in range(1,len(name)+1):
    print((name[:i]).upper())
