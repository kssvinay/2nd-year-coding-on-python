n=int(input())
A=[]
B=[]
for i in range(0,n):
    l=[]
    for j in range(0,n):
        x=int(input())
        l.append(x)
    A.append(l)
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            B.append(A[i][j])
print("The maximum element form primary and secondary diagnal is",max(B))
print(max(B))
