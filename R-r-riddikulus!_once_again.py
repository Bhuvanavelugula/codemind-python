a,b=map(int,input().split())
L=list(map(int,input().split()))
for i in range(b):
    L.append(L[i])
print(*L[b:])