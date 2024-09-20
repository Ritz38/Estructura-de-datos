from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.paulina = -1
        #resto de atributos
        
        
def BFS(nodes, edges, start):
    nodes[start].visited = True
    nodes[start].paulina = 0
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].paulina = nodes[a].paulina + 1
                nodes[b].visited = True
                q.append(b)
        
casos = int(input())
for fiesta in range(casos):
    I, B = list(map(int,input().split(", ")))
    
    aristas = {}
    nodos = {}
    
    for j in range(I):
        nodos[j] = Node()

    for i in range(B):
        a, b = list(map(int, input().split()))
        
        if a not in aristas:
            aristas[a] = set([b])
        else: 
            aristas[a].add(b)
            
        if b not in aristas:
            aristas[b] = set([a])
        else: 
            aristas[b].add(a)
            
    BFS(nodos,aristas,0)
        
    print(f"fiesta {fiesta+1}:")
    for k in range(1,I):
        pau = nodos[k].paulina
        if pau == -1:
            print(k, "INF")
        else:
            print(k, pau)
    if not fiesta == casos-1:
        print("")
    
    
    
        
    