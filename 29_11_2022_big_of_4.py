a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))
d = int(input("enter a number : "))
if a>b and a>c and a>d:
    print("a is big")
elif b>a and b>c and b>d:
    print("b is big")
elif c>a and c>b and c>d:
    print("c is big")
elif d>a and d>b and d>c:
    print("d is big")
else:
    print("all are equal")
