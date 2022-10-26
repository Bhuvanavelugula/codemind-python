n,r,q=map(int,input().split())
L=list(map(int,input().split()))
p=[]
for i in range(q):
    t=int(input())
    p.append(t)
t=L[len(L)-r:]
L=t+L
for i in p:
    print(L[i])