num=int(input())
L=list(map(int,input().split()))
x=int(input())
L1=[]
for i in range(len(L)):
    if L[i]==x:
        L1.append(i)
if(len(L1)!=0):
    print(L1[0],L1[-1])
else:
    print(-1,-1)