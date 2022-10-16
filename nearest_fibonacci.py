n=int(input())
a=0
b=1
c=0
L=[0,1]
L1=[]
L2=[]
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    L.append(c)
for i in range(len(L)):
    if L[i]<n:
        L1.append(L[i])
    else:
        L2.append(L[i])
if n in L:
    L.remove(n)
x=max(L1)
y=min(L2)
d1=n-max(L1)
d2=min(L2)-(n)
if(d1==d2):
   print(x,y)
elif(d1<d2):
    print(x)
else:
    print(y)