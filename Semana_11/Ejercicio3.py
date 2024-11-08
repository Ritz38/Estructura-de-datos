from collections import deque

class Node():
    def __init__(self):
        self.visited = False


def BFS(nodes, edges):
    c=0
    mayor=0
    for i in nodes:
        if nodes[i].visited == False:
            c+=1
            nodes[i].visited = True
            q = deque()
            q.append(i)
            c2=0
            
            while q:
                a = q.popleft()
                c2+=1
                for b in edges[a]:
                    if nodes[b].visited == False:
                        nodes[b].visited = True
                        q.append(b)
            if c2>mayor:
                mayor = c2
    return [c,mayor]
            

for _ in range(int(input())):
    R = int(input())
    
    nodos = {}
    aristas = {}
    
    for i in range(R):
        x, y = list(map(int,input().split()))
        
        if x not in nodos:
            nodos[x] = Node()
        if y not in nodos:
            nodos[y] = Node()
        
        
        if x not in aristas:
            aristas[x] = set([y])
        else:
            aristas[x].add(y)
            
        if y not in aristas:
            aristas[y] = set([x])
        else:
            aristas[y].add(x)
    
    print(*BFS(nodos,aristas))