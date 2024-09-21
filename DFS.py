from collections import deque

def DFS(nodes, edges, start):
    nodes[start].visited = True
    stack = deque()
    stack.append(start)
    while stack:
        a = stack.pop()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].visited = True
                stack.append(b)



