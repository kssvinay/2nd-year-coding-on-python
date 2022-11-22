p = int(input("enter principal amount"))
t = int(input("enter time period"))
r = float(input("enter rate of interest"))
si = (p*t*r)/100
emi = (si+p)/(t*12)
print("The emi for the given amount is", emi)
