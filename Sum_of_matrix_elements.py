a=int(input())
b=int(input())
L=[]
for i in range(a):
    t=list(map(int,input().split()))
    L.append(t)
s=0
for i in L:
    s+=sum(i)
print(s)