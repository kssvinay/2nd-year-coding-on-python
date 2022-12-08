#sum of factorial of n numbers 1!+2!+3!+4!....+n!
n = int(input())
sum = 0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact  = fact *j
    sum += fact
    print(i , fact)
print("sum", sum)
