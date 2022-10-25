n=int(input())
L=[]
for i in range(n):
    s=input()
    if s=="++X" or s=="X++":
        L.append(1)
    elif s=="--X" or s=="X--":
        L.append(-1)
print(sum(L))