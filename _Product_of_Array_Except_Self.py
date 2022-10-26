n=int(input())
L=list(map(int,input().split()))
r=[]
for i in range(len(L)):
    p=1
    if(L[i]>=1):
        t=i
        for j in range(len(L)):
            if(j==t):
                continue
            else:
                p=p*L[j]
        print(p,end=" ")
    else:
        print(L[j],end=" ")