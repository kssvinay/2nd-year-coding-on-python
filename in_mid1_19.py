#Assignment-19:
#Write a program to print square root of the given number.
#If square root is greater than 10,print 'Hello' otherwise
# print 'Hi'
  
num = int(input())
print(num**(1/2))
if num>=100:
    print("Hello")
else:
    print("Hi")
