def fun(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if(L[i]>L[j]):
                return False
        return True
num=int(input())
for i in range(num):
    n=int(input())
    L=list(map(int,input().split()))
    if fun(L):
        print(0)
    else:
        print(max(L)-min(L))