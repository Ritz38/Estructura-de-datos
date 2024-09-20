N, T = map(int,input().split())

a = {}
resultados = []


for i in range(N):
    entrada = int(input())
    a[entrada] = [entrada]
    
    
for k in a:
    for j in a:
        tercero = T-(j+k)
        if j != k and (len(a[j])==1 and sum(a[j]+[k]+[tercero])==T) and tercero!=j and tercero!=k:
            a[j]+=[k]
            if len(a[j])==3:
                resultados += [[sorted(a[j]),j]]
    for k in resultados:
        print(*k[0])
        a.pop(k[1])
    
