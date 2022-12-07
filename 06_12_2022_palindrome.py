num=int(input("Enter a number:"))
n=num
s=0
while(num>0):
    t=num%10
    s=s*10+t
    num=num//10
if(n==s):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
