from collections import deque
x = deque(map(int,input().split()))
revendedores = deque()

for _ in range(x[0]):
    revendedores.append(tuple(map(int,input().split())))

c=0

while True:
    if len(revendedores)==0:
        print("quedaron boletas disponibles")
        exit(0)
    if (x[1]-revendedores[0][1])>0:
        if c==4:
            x.append(x.pop()-revendedores[0][1])
            revendedores.popleft()
            c=0
        else:
            x.append(x.pop()-revendedores[0][1])
            revendedores.append(revendedores.popleft())
            c+=1
    else:
        print(revendedores[0][0], x[1])
        exit(0)