from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        #resto de atributos

def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    q.append(-1)
    while q:
        if q == -1:
             
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].visited = True
                q.append(b)


nodos = {}

for j in range(int(input())):
        nodos[j] = Node()


