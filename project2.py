import heapq

def prim(graph, start):
    V = len(graph)
    
    visited = [False] * V
    key = [float('inf')] * V
    parent = [-1] * V
    
    pq = [(0, start)]  
    key[start] = 0
    
    while pq:
        weight, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        for v, weight in graph[u]:
            if not visited[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))
    
    return parent

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7)]
}

start = 0
parent = prim(graph, start)

print("Parent array for MST:", parent)