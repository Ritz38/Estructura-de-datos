from bisect import bisect_right 
fila=[]
tiempos=[]
while True:
    a, b =list(input().split())
    if a == "0":
        break
    fila.append(a)
    tiempos.append(int(b))
    limite=min(tiempos)

    if len(fila) > limite:
     if tiempos.count(limite) > 1:
        index = bisect_right(tiempos, limite)-1
        fila.pop(index)
        tiempos.pop(index)
     else:
        index = tiempos.index(limite)
        fila.pop(index)
        tiempos.pop(index)
print(len(fila))