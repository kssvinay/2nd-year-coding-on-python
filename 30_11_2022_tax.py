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
bill = (t*tc)+(o*oc)+(b*bc)+(s*sc)
if bill>3000:
  tax = 0.05*bill
elif bill>2000:
  tax = 0.07*bill
elif bill>1000:
  tax = 0.1*bill
elif bill>500:
  tax = 0.15*bill
else:
  tax = 100
print("Phone number: ",cphno)
print("name: ",name)
print("address :",address)
print("tax: ",tax)
print(" your bill amount : ",bill)
