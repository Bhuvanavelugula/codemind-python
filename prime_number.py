n=int(input())
C=0
for i in range(1,n+1):
    if n%i==0:
        C+=1
if C==2:
    print("prime")
else:
    print("not a prime")