n=int(input())
for x in range(n):
    s=int(input())
    s=str(s)
    L=[]
    r=[]
    for t in s:
        L.append(int(t))
    m=min(L)
    mm=max(L)
    for i in range(m,mm+1):
        r.append(i)
    L.sort()
    if L==r:
        print("YES")
    else:
        print("NO")