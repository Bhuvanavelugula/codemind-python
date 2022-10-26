num=int(input())
for i in range(num):
    n=int(input())
    L=list(map(int,input().split()))
    x=len(L)//2
    t=L[x]
    L1=[]
    for j in range(x):
        L1.append(max(L))
        L.remove(max(L))
        L1.append(min(L))
        L.remove(min(L))
    if(len(L)%2==0):
        print(*L1)
    else:
        L1.append(t)
        print(*L1)