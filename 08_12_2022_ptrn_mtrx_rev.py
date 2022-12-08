n = int(input("enter rows"))
m = int(input("enter columns"))
k=m*n
for i in range(1,n+1):
	for j in range(1,m+1):
		print(k,end=" ")
		k=k-1
	print()
