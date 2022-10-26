n=int(input())
L=list(map(int,input().split()))
n=n//2
L1=[]
L2=[]
for i in range(n):
    L1.append(L[i])
for i in range(n,len(L)):
    L2.append(L[i])
for i in range(len(L1)):
    print(L1[i],L2[i],end=" ")