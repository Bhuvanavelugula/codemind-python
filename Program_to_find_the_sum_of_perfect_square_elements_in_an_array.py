n=int(input())
L=list(map(int,input().split()))
t=max(L)
L1=[]
for i in range(1,t+1):
    L1.append(i**2)
s=0
for i in L:
    if i in L1:
        s+=i
print(s)