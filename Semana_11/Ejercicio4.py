from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.color = -1

def BFS(nodes, edges, start):
    queue = deque([start])
    nodes[start].visited = True
    nodes[start].color = 0
    
    while queue:
        current = queue.popleft()
        current_color = nodes[current].color
        
        for neighbor in edges[current]:
            if not nodes[neighbor].visited:
                nodes[neighbor].color = 1 - current_color
                nodes[neighbor].visited = True
                queue.append(neighbor)
            elif nodes[neighbor].color == current_color:
                return False
    return True



for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    
    nodos = {}
    aristas = {}

    for i in range(M):
        x, y = list(map(int,input().split(", ")))
        
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



    bipartito = True
    for i in nodos:
        if not nodos[i].visited:
            if not BFS(nodos, aristas, i):
                bipartito = False
                break
    
    if bipartito:
        print("bipartito")
    else:
        print("no bipartito")

            
    