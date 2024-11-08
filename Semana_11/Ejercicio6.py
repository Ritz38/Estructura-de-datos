from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.saltos = 0
        
        

def BFS(nodes, start, end):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        if a == end: break
        if a[0] in "CDEF":
            if a[1] in "3456":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [TL,TR,RT,RB,BL,BR,LT,LB]
                
            elif a[1] == "1":
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                edges = [TR,RT,RB,BR]
            
            elif a[1] == "2":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                edges = [TL,TR,RT,RB,BL,BR]
                
            elif a[1] == "7":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [TL,TR,BL,BR,LT,LB]
                
            else:
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [TL,BL,LT,LB]
                
                
                
                
                
                
        elif a[0] == "A":
            if a[1] in "3456":
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [RB,BL,BR,LB]
                
            elif a[1] == "1":
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                edges = [RB,BR]
            
            elif a[1] == "2":
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                edges = [RB,BL,BR]
                
            elif a[1] == "7":   
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"

                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [BL,BR,LB]
                
            else:
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [BL,LB]
                
                
                
                
        elif a[0] == "B":
            if a[1] in "3456":
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [RT,RB,BL,BR,LT,LB]
                
            elif a[1] == "1":             
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                edges = [RT,RB,BR]
            
            elif a[1] == "2":
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                edges = [RT,RB,BL,BR]
                
            elif a[1] == "7":      
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                BR = f"{letras[letras.index(a[0])+2]}{int(a[1])+1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [BL,BR,LT,LB]
                
            else:
                BL = f"{letras[letras.index(a[0])+2]}{int(a[1])-1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [BL,LT,LB]
        
        
        
        
        elif a[0] == "G":
            if a[1] in "3456":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [TL,TR,RT,RB,LT,LB]
                
            elif a[1] == "1":
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
                
                edges = [TR,RT,RB]
            
            elif a[1] == "2":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                RB = f"{letras[letras.index(a[0])+1]}{int(a[1])+2}"
 
                edges = [TL,TR,RT,RB]
                
            elif a[1] == "7":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [TL,TR,LT,LB]
                
            else:
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                LB = f"{letras[letras.index(a[0])+1]}{int(a[1])-2}"
                
                edges = [TL,LT,LB]
                
        elif a[0] == "H":
            if a[1] in "3456":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                
                edges = [TL,TR,RT,LT]
                
            elif a[1] == "1":
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
            
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                edges = [TR,RT]
            
            elif a[1] == "2":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                RT = f"{letras[letras.index(a[0])-1]}{int(a[1])+2}"
                edges = [TL,TR,RT]
                
            elif a[1] == "7":
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                TR = f"{letras[letras.index(a[0])-2]}{int(a[1])+1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                
                edges = [TL,TR,LT]
                
            else:
                TL = f"{letras[letras.index(a[0])-2]}{int(a[1])-1}"
                
                LT = f"{letras[letras.index(a[0])-1]}{int(a[1])-2}"
                
                edges = [TL,LT]
            
            
                
                
                
        
        for b in edges:
            if nodes[b].visited == False:
                nodes[b].saltos = nodes[a].saltos + 1
                nodes[b].visited = True
                q.append(b)
    return nodes[a].saltos

def reiniciarNodos():
    for k in nodos:
        nodos[k] = Node()

letras = ["A","B","C","D","E","F","G","H"]

nodos = {}


for i in letras:
    for j in range (1,9):
        nodos[f"{i}{j}"] = Node() 


for _ in range(int(input())):
    inicio, final = input().split()
    print(BFS(nodos, inicio, final))
    reiniciarNodos()
    