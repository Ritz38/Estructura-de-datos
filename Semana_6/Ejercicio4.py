import heapq
for _ in range(int(input())):
    v = int(input())
    c = input().split()
    heapq.heapify(c)
    C=0
    i=True
    x=""
    y=""
    while C<v:
        if i:
            i=False
            x+=heapq.heappop(c)
        else:
            i=True
            y+=heapq.heappop(c)
        C+=1
    print(int(x)+int(y))