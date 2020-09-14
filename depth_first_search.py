# An implementation of the depth-first search algorithm
# But actually this script calculates the number of components in the graph using 
# depth-first search
'''
ALGORITHM DESCRIPTION
1) Visit the vertex x;
2) Mark it as visited;
3) Move to some adjacent vertex of x;
4) Repeat the same 1, 2 steps

'''
import numpy as np

v, e = map(int, input().split())
graph_adj = [[] for i in range(v)]

for i in range(e):
     v1, v2 = map(int, input().split())
     graph_adj[v1 - 1].append(v2-1)
     graph_adj[v2 - 1].append(v1-1)

print(graph_adj)
def depth_first_search(graph, current_vertex, visited):
    # mark vertex as visited
    visited.add(current_vertex)
    if graph[current_vertex]:
        for i in set(graph[current_vertex]) - visited: # it will only visit adjacent vertices that are not visited yet
            depth_first_search(graph, i, visited)
        return visited

num_components = 0
visited_vertices = set()
vertices = set(i for i in range(len(graph_adj)))

num_components = 0
while len(vertices) > 1:
    visited_vertices = depth_first_search(graph_adj, next(iter(vertices)), visited_vertices)
    num_components += 1
    vertices -= visited_vertices
    if len(vertices) == 1:
        num_components += 1

print(num_components)



