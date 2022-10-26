n=int(input())
L=list(map(int,input().split()))
x=int(input())
if x not in L:
    print(-1)
else:
    print(L.index(x))