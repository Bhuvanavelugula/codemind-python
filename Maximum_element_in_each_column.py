a,b=map(int,input().split())
L=[]
for i in range(a):
    t=list(map(int,input().split()))
    L.append(t)
for i in range(len(L)):
    r=[]
    for j in range(len(L)):
        r.append(L[j][i])
    print(max(r))