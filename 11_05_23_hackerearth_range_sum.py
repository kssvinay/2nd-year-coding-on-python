t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    pf=[0]*(n+1)
    for i in range(1,n+1):
        pf[i]=pf[i-1]+arr[i-1]
    q=int(input())#3
    while(q>0):
        l,r=map(int,input().split())
        print(pf[r]-pf[l-1])
        q=q-1
