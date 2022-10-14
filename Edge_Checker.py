n,m=map(int,input().split())
if n==m+1or n==m-1:
    print("Yes")
elif(n==1 and m==10) or(n==10 and m==1):
    print("Yes")
else:
    print("No")