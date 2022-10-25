n=int(input())
L=list(map(int,input().split()))
L1=L[:len(L)//2]
L2=L[len(L)//2:]
L2=L2[::-1]
print(*(L2+L1))