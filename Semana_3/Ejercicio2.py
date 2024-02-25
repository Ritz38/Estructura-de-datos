from bisect import bisect_left, bisect_right 
C=int(input())
for i in range(C):
    N=tuple(sorted(map(int,input().split())))
    s=()
    n=len(N)
    i=0
    while i<n:
        p=len(N[bisect_left(N,N[i]):bisect_right(N,N[i]):])
        s+=(p,)
        i+=p
    print(*s)