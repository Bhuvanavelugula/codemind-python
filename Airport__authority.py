n=int(input())
L=[]
for i in range(n):
    t=int(input())
    L.append(t)
s=0
t=int(input())
for i in L:
    if i>t:
        s+=2
    else:
        s+=1
print(s)