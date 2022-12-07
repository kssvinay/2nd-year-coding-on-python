num = int(input())
rev = 0

while num != 0:
    t = num % 10
    rev = rev * 10 + t
    num //= 10

print("Reversed Number: " ,rev)
