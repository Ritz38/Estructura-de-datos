from collections import deque
N=int(input())
for _ in range(N):
    pro=deque(input().split())
    pro.pop()
    pila = deque()
    c=0
    for i in pro:
        if i in "([{":
            pila.append(i)
        elif len(pila)==0:
            print("incorrecta")
            c+=1
            break
        elif (i==")" and pila[-1]!="(") or (i=="]" and pila[-1]!="[") or (i=="}" and pila[-1]!="{"):
            print("incorrecta")
            break
        else:
            pila.pop()
    if len(pila)==0 and c==0: print("correcta")