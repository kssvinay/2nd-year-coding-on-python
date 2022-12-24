
def is_prime(num):
    ans = False
    cnt=0
    for i in range(1,num+1):
        if num%i ==0 :
            cnt+=1
    if cnt==2:
        ans=True
    return ans

num_start = int(input())
num_end = int(input())
for i in range(num_start,num_end):
    if is_prime(i):
        print(i)
