n=int(input())
L=list(map(int,input().split()))
if max(L)>=n:
    print("NO")
else:
    print("YES")