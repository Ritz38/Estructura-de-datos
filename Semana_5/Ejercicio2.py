C=int(input())
for _ in range(C):
    x,k=map(int,input().split())
    l=list(range(1,x+1))
    jugadores= x
    pos=0
    while jugadores>1:
        pos = (pos + k - 1) % jugadores
        jugadores-=1
        k = l.pop(pos) % jugadores
        if k == 0: k = 1
    print(l[0])