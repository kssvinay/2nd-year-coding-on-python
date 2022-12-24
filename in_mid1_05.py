#Assignment-5:
#Write a program to print given number is prime or not.

num = int(input())
cnt=0
for i in range(1,num+1):
    if num%i ==0 :
        cnt+=1
if cnt==2:
    print(num,"is a prime number")
else:
    print(num, "is not a prime number")
