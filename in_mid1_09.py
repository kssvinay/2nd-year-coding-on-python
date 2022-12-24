#Assignment-9:
#Write a program to print sum of n febnocci  series?

n = int(input())
a, b,c  = 0, 1,0
sum=0
print("Fibonacci sequence:")
while c <= n:
  print(c)
  sum+=c
  c= a + b
  a = b
  b = c
print(sum)
