C=int(input())
for _ in range(C):
    N=tuple(map(int,input().split()))
    n=len(N)
    c=0
    while True:
        v=True
        for j in range(n-1):
            if N[j]>N[j+1]:
                N=N[0:j:]+(N[j+1],)+(N[j],)+N[j+2::]
                c+=1
                v=False
        if v:
            break
    print(c)