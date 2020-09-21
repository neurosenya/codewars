import numpy as np
import random

v, e = map(int, input().split())
graph_adj = [[] for i in range(v)]

for i in range(e):
     v1, v2 = map(int, input().split())
     graph_adj[v1 - 1].append(v2-1)
     graph_adj[v2 - 1].append(v1-1)


#graph_adj = [sorted(i, reverse=True) for i in graph_adj]
def connectivity_check(graph_adj, e, v):
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
        if not visited_vertices and num_components != 0:
            break
        visited_vertices = depth_first_search(graph_adj, next(iter(vertices)), visited_vertices)
        num_components += 1
        if visited_vertices:
            vertices -= visited_vertices
            if len(vertices) == 1:
                num_components += 1
    if num_components > 1:
        return None
    else:
        return num_components

def even_degree_nodes(graph_adj):
    for i in graph_adj:
        if len(i) % 2 != 0 and len(i) != 0:
            return False
    return True

def eulers_cycle(graph_adj, v, e):
    if e==1 and v==1:
        return 'NONE'
    if e==0:
        return 'NONE'
    if not connectivity_check(graph_adj, v, e):
        return 'NONE'
    if not even_degree_nodes(graph_adj):
        return 'NONE'

    eulers_cycle = [0]
    node = random.randint(0, v-1)
    S = []
    S.append(node)
    result = []
    while S:
        if graph_adj[S[-1]]:
            current_node = S[-1]
            adj_node = graph_adj[S[-1]][-1]
            S.append(adj_node)
            graph_adj[current_node].remove(adj_node)
            graph_adj[adj_node].remove(current_node)
        else:
            last_node = S.pop()
            result.append(last_node)
    if result[0] != result[-1]:
        return 'NONE'
    if result:
        return [i+1 for i in result[:-1]]

answer = eulers_cycle(graph_adj, v, e)

if answer == 'NONE':
    print(answer)
else:
    for i in answer:
        print(i, end=' ')
