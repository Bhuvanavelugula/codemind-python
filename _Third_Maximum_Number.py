n=int(input())
L=list(map(int,input().split()))
L=set(L)
L=list(L)
L.sort()
if len(L)<3:
    print(max(L))
else:
    print(L[-3])