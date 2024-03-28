import heapq
C=int(input())
for _ in range(C):
    N=list(map(int,input().split()))
    heapq.heapify(N)
    heapq.heappop(N)
    while len(N)>2: heapq.heappush(N,heapq.heappop(N)+heapq.heappop(N))
    print(*N)