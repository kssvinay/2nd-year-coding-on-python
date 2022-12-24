#Assignment -7:
#Write a program to print given number is perfect or not?

num = int(input())
fact = 0
for i in range(1,num+1):
    if num%i ==0 :
        fact += i
if fact == 2*num:
    print("perfect number")
else:
    print("not a perfect number")
