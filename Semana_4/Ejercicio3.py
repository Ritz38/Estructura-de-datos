from collections import deque
uroboro = deque()
while True:
    msj = deque(input().split())
    if msj[0]=="termina": break
    elif msj[0]=="agrega": uroboro.append(int(msj[1]))
    else:
        if uroboro[-1]>=uroboro[0]:
            uroboro.popleft()
        else: uroboro.pop()
if len(uroboro)>0:
    print("cabeza", uroboro[0],"cola",uroboro[-1])
else:
    print("uroboro vacio")