# Implementation of the breadth-first search algorithm 
# for finding the distance from the root to each vertix
from collections import deque
from collections import OrderedDict

v, e = map(int, input().split())
graph_adj = [[] for i in range(v)]

# constructing list where each sublist contains 
# all adjacent vertices for vertice (index + 1)
visited_order = []
for i in range(e):
    v1, v2 = map(int, input().split())
    if v1 not in visited_order:
        visited_order.append(v1)
    graph_adj[v1].append(v2)
    graph_adj[v2].append(v1)


# Initialize queue 
q = deque()
# append there first vertex
q.append(0)
visited = [False for i in range(v)]
result = OrderedDict({key: 0 for key in range(v)})
visited[0] = True

while q:
    current_vertex = q.popleft()
    adjacent_vertices = graph_adj[current_vertex]
    for vertex in adjacent_vertices:
        if visited[vertex] == False:
            q.append(vertex)
            result[vertex] = result[current_vertex] + 1
            visited[vertex] = True

for k, v in result.items():
    print(v, end=' ')
