from bisect import bisect_left
C=int(input())
for _ in range(C):
    x=tuple(map(int,input().split()))
    y=tuple(map(int,input().split()))
    p=()
    c=0
    for i in range(1,x[1]+1):
        if x[1]%i==0:
            p+=(i,)
    for j in p:
        v=bisect_left(y,j)
        if v!=len(y) and y[v]==j:
            c+=1
    if c==len(p):
        print("Es PrimiConjunto")
    else: print("No es PrimiConjunto")