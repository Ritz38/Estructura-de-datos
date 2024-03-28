import heapq
for _ in range(int(input())):
    c=list(map(int,input().split()))
    jugadores=list(range(1,c[0]+1))
    while c[0]>1:
        jugadores_1 = []
        for i in jugadores: 
            heapq.heappush(jugadores_1,(i*c[1])%c[2])
        jugadores = jugadores_1
        for _ in range(c[0]//2): 
            heapq.heappop(jugadores)
            c[0]-=1
    print(heapq.heappop(jugadores))