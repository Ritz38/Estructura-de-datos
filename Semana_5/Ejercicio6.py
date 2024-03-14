fila=[]

while True:
    d, m = input().split()
    if d=="0" and m=="0": break
    m=int(m)
    if len(fila)<m: fila.append(m)
    fila.sort()
    if len(fila)>fila[0]:fila.pop(0)
print(len(fila))