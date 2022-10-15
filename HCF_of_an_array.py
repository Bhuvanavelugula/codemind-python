n=int(input())
L=list(map(int,input().split()))
n=max(L)
t=[]
for i in range(1,n+1):
    c=0
    for j in L:
        if j%i==0:
            c+=1
    if c==len(L):
        t.append(i)
print(max(t))