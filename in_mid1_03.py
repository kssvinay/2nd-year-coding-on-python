#Assignment-3:
#Write a program to print Fibonacci  n series?
n = int(input())

a, b,c  = 0, 1,0

print("Fibonacci sequence:")
while c <= n:
  print(c)
  c= a + b
  a = b
  b = c
