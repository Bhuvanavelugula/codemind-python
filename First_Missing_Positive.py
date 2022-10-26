n=int(input())
L=list(map(int,input().split()))
x=1
while True:
    if x not in L:
        print(x)
        break
    else:
        x+=1