tl = 20
b = 5
ac = 200
fr = 50
tlt = int(input("Enter how many hours you use tubelight"))
bt = int(input("Enter how many hours you use bulb"))
act = int(input("Enter how many hours you use AC"))
frt = int(input("Enter how many hours you use fridge"))
energy = (tl*tlt)+(b*bt)+(ac*act)+(fr*frt)
#1kwh = 2rupees
#so cost = energy *2
cost = energy*2
print("Your tubelight energy connection",tlt*tl)
print("Your bulb energy connection",bt*b)
print("Your AC energy connection",act*ac)
print("Your fridge energy connection",frt*fr)
print("Your total energy consumption is",energy)
print("Your electricity bill is",cost,"rupees")
