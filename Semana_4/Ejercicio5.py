from collections import deque
C=int(input())
for _ in range(C):
    cant = deque(map(int,input().split()))
    pet = deque(map(int,input().split()))
    N = cant[1]
    t=0
    while True:
        if pet[0]==0:
            while pet[0]==0:
                pet.popleft()
                N-=1
            pet.append(pet.popleft()-1)
        else:
            pet.append(pet.popleft()-1)
        t+=5
        if N==1:
            if pet[-1]==0: break
            else: N=len(pet)
        else: N-=1
    print(t)