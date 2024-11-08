from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.dia = -1
        #resto de atributos

def BFS(nodes, edges, start):
    nodes[start].visited = True
    nodes[start].dia = 0
    dias = {}
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].dia = nodes[a].dia + 1
                if nodes[b].dia not in dias:
                    dias[nodes[b].dia] = 1
                else:
                    dias[nodes[b].dia]+=1
                nodes[b].visited = True
                q.append(b)
    if not dias:
        return [-1]
    else:
        diaMax = max(dias,key=dias.get)
        return [diaMax, dias[diaMax]]

def reinicioNodos():
    for j in range(entrada):
        nodos[j] = Node()


entrada = int(input())

nodos = {}
aristas = {}


        


for i in range(entrada):
    aristas[i] = set(map(int,input().split()))
    if -1 in aristas[i]:
        aristas[i] = set()
    
for k in list(map(int,input().split(", "))):
    reinicioNodos()
    a = BFS(nodos,aristas,k)
    if a[0]==-1:
        print(0)
    else:
        print(a[0], a[1])

