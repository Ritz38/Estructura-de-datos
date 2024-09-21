# c & d Interseccion
# c | d Union
# c - d Diferencia
# c ^ d Diferencia simetrica
# c <= d Subconjunto
# c < d Subconjunto propio


N, Q = list(map(int,input().split()))

eventos = list(map(int, input().split()))

eventosDiccionario = {}

for i in eventos:
    if i in eventosDiccionario:
        eventosDiccionario[i]+=1
    else:
        eventosDiccionario[i]=1

for j in range(Q):
    x,y = list(map(int,input().split()))

    if x in eventosDiccionario:
        if eventosDiccionario[x] >= y:
            print("SI")
        else:
            print("NO")
    else:
        if y==0: print("SI")
        else: print("NO")

