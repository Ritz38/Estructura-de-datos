import heapq
t=int(input())
tonos=int(input())
m=[]
for _ in range(tonos):
    ton=list(map(int,input().split()))
    ls=[x for x in range(ton[1],t+1,ton[2])]
    for i in ls: heapq.heappush(m,i)
for _ in range(len(m)):print(heapq.heappop(m))