L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
a=0
b=0
for i in range(len(L1)):
    if L1[i]>L2[i]:
        a+=1
    elif L1[i]<L2[i]:
        b+=1
print(a,b)