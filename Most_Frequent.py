n=int(input())
L=list(map(int,input().split()))
s=set(L)
s=list(s)
m=0
c=0
for i in range(len(s)):
    if L.count(s[i])>m:
        m=L.count(s[i])
        t=s[i]
print(t)