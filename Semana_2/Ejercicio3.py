C=int(input())
for i in range(C):
    p=tuple(input().split())
    p=p[::-1]
    r=""
    for j in range(0,len(p),2):
        if len(p)%2!=0 and j==len(p)-1: 
            r+=p[j]
            break
        r+=p[j+1]+p[j]
    print(r)
 