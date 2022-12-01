t = 20
o = 40
b = 60
s = 20
cphno = input("Enter your phn number : ")
name = input("enter your name : ")
address = input("enter your address : ")
tc = int(input("How many tomatoes you want in kgs?"))
oc = int(input("How many onions you want in kgs?"))
bc = int(input("How many biscuits packets you want?"))
sc = int(input("How many soaps you want?"))
cpn = input("Enter your coupon code : ")
bill = (t*tc)+(o*oc)+(b*bc)+(s*sc)
if bill > 3000:
  tax = 0.05 * bill
elif bill > 2000:
  tax = 0.07 * bill
elif bill > 1000:
  tax = 0.1 * bill
elif bill > 500:
  tax = 0.15 * bill
else:
  tax = 100
bill = tax + bill
if cpn == "DIWALI":
  if bill >= 5000:
    dis = 0.1 * bill
  elif bill >= 3000:
    dis = 0.06 * bill
  elif bill >= 1000:
    dis = 0.04 * bill
  elif bill > 500:
    dis = 0.15 * bill
  else:
    dis = 0
elif cpn == "CHRISMAS":
  if bill > 3000:
    dis = 0.2 * bill
  elif bill > 2000:
    dis = 0.1 * bill
  elif bill > 1000:
    dis = 0.05 * bill
  else:
    dis = 0
else:
  dis=0
bill = bill-dis
print("Phone number: ",cphno)
print("name: ",name)
print("address :",address)
print("tax: ",tax)
print("discount of rupees",dis,"is added to your bill")
print(" your bill amount : ",bill)
