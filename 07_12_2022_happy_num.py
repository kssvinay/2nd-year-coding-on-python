def sumof(n):
    sum = 0
    while n != 0:
        sum += (n % 10) ** 2
        n //= 10
    print(sum)
    if( sum ==1 ):
        return True
    else:
        if sum == 2 or sum==3 or sum==4 or sum==5 or sum==5 or sum==8 or sum==9:
            return False
        else:
            return sumof(sum)

n = int(input())
if(sumof(n)):
    print(n,"is a happy number")
else:
    print(n,"is not a happy number")
