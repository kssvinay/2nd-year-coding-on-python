a = int(input("enter first number"))
b = int(input("enter second number"))
print("the numbers before swapping are",a,b)
a = a + b
b = a - b
a = a - b
print("the numbers after swapping are",a,b)