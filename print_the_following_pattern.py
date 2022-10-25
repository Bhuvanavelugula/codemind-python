n=int(input())
L="ZXCVBNMLKJHGFDSAQWERTYUIOP"
L=list(L)
L.sort()
for i in range(n):
    for _ in range(n):
        print(L[i],end=" ")
    print()