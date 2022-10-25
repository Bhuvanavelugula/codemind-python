def fun(x):
    x=list(x)
    s=""
    for i in x:
        s+=i
    return s
n= int(input())
s=""
for i in range(n):
    L=[]
    for j in range(n):
        if i==j:
            L.append("0")
        else:
            L.append("x")
    print(fun(L))