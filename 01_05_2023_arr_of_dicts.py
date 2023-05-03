player = []
n = int(input("Enter Number of players: "))
for i in range(n):
    k = {}
    k['pno'] = input("Enter Player Number: ")
    k['pname'] = input("Enter Player Name: ")
    player.append(k)
print(player)

