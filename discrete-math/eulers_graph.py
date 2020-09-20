import numpy as np

v, e = map(int, input().split())
graph_adj = [[] for i in range(v)]

for i in range(e):
     v1, v2 = map(int, input().split())
     graph_adj[v1 - 1].append(v2-1)
     graph_adj[v2 - 1].append(v1-1)


graph_adj = [sorted(i, reverse=True) for i in graph_adj]
def eulers_cycle(graph_adj, e, v):
    if e == 0 or v == 0:
        return 'NONE'
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
        return 'NONE'

    eulers_cycle = [0]
    node = 100000
    for i, n in enumerate(graph_adj):
        if len(n) < node:
            node = i
    #print(graph_adj)
    for i in graph_adj:
        if len(i) % 2 != 0:
            return 'NONE'
    while len(eulers_cycle) < e: # while cycle did not go through all edges
        if graph_adj[node]:
            next_node = graph_adj[node].pop()
            graph_adj[next_node].remove(node)
            #print(graph_adj)
            if graph_adj[next_node]:
                node = next_node
                eulers_cycle.append(node)
            check = [True if i==[] else False for i in graph_adj]
            if all(check):
                #print(check)
                eulers_cycle.append(next_node)
                break
        else:
            for i in graph_adj:
                if i:
                    node = graph_adj.index(i)
    return [i+1 for i in eulers_cycle]

answer = eulers_cycle(graph_adj, e, v)
if answer == 'NONE':
    print(answer)
else:
    for i in answer:
        print(i, end=' ')

