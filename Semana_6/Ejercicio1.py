import heapq
a=[]
while True:
    x=input()
    if x=="end": 
        print(re)
        break
    elif x=="sig":
        if len(a)>0: re=heapq.heappop(a)
    else: 
        heapq.heappush(a, int(x))