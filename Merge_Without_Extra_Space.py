n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    L1=list(map(int,input().split()))
    L2=list(map(int,input().split()))
    L=L1+L2
    L.sort()
    print(*L)