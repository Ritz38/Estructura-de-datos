from collections import deque

def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].paulina = nodes[a].paulina + 1
                nodes[b].visited = True
                q.append(b)