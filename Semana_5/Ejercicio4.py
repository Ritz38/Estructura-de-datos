cuarto=[]
while True:
    k=int(input())
    if k == 0: break
    if k in cuarto: cuarto.remove(k)
    elif k+1 in cuarto: cuarto.remove(k+1)
    elif k-1 in cuarto: cuarto.remove(k-1)
    else: cuarto.append(k)
if not cuarto: print(0)
else: print(*cuarto)