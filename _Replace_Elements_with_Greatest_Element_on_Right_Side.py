n=int(input())
L=list(map(int,input().split()))
L1=[]
for i in range(len(L)-1):
    t=L[i+1:]
    L1.append(max(t))
L1.append(-1)
print(*L1)