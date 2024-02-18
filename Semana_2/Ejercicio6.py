C = int(input())
for i in range(C):
    T=int(input())
    J=tuple(map(int,input().split()))
    i=0
    c=()
    while True:
        if i>len(J)-1 or i<0:
            break
        c+=(i,)
        if c.count(c[-1])==2:
            c=c[:len(c)-1:]
            break
        i=i+J[i]
    print(len(c))