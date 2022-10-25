n=int(input())
L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L=list(L)
for i in range(n,0,-1):
    for _ in range(i):
        print(L[i-1],end=" ")
    print()