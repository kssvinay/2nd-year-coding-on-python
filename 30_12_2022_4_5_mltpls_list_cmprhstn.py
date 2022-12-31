n = int(input("enter limit"))
l = [i for i in range(1,n) if i%4==0 or i%5==0]
print(l)
