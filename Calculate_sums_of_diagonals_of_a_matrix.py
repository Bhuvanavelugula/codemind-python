num=int(input())
L=[]
for i in range(num):
    t=list(map(int,input().split()))
    L.append(t)
fd=0
sd=0
L1=[]
for i in range(len(L)):
    L1.append(L[i][::-1])
for i in range(len(L)):
    for j in range(len(L)):
        if(i==j):
            fd+=L[i][j]
            sd+=L1[i][j]
print("Principal Diagonal:",end="")
print(fd)
print("Secondary Diagonal:",end="")
print(sd)