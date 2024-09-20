aristas = {}

a, b = list(map(int, input().split()))
aristas[a] = aristas[a] | set([b]) 
aristas[b] = aristas[b] | set([a])
print(aristas[a])
print(aristas[b])