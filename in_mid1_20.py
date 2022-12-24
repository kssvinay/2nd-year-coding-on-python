#Assignment-20:
#Write a program to maximum prime number and minimum prime number from the given list.

def is_prime(num):
    ans = False
    cnt=0
    for i in range(1,num+1):
        if num%i ==0 :
            cnt+=1
    if cnt==2:
        ans=True
    return ans

l = list(map(int,input().split()))
sr = sorted(l)
for i in sr:
    if is_prime(i):
        print(i,"is min prime")
        break
for j in sr[::-1]:
    if is_prime(j):
        print(j,"is max prime")
        break
