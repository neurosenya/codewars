'''
Description of the algorithm:
1) Check whether graph is fully connected
2) Check whether all nodes have even degree
3) Fleury's algorithm:
    - Start from node 0 (it doesn't matter from which node to start if you have only even degree nodes
    - Follow edges one at a time. Try not to go through nodes that connect two subgraphs
    - Stop when there are no unvisited edges
'''
import numpy as np
import random

v, e = map(int, input().split())
graph_adj = {i:[] for i in range(v)}
for i in range(e):
     v1, v2 = map(int, input().split())
     graph_adj[v1 - 1].append(v2-1)
     graph_adj[v2 - 1].append(v1-1)

print(graph_adj)

def depth_first_search(graph, current_vertex, visited):
    visited.add(current_vertex)
    if graph[current_vertex]:
        for i in set(graph[current_vertex]) - visited: # it will only visit adjacent vertices that are not visited yet
            depth_first_search(graph, i, visited)
        return visited

def connectivity_check(graph_adj, e, v):
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
    return num_components

print(connectivity_check(graph_adj, v, e))

def even_degree_nodes(graph_adj):
    for i in graph_adj:
        if len(i) % 2 != 0 and len(i) != 0:
            return False
    return True

def eulers_cycle(graph_adj, v, e):
    if e==0:
        return 'NONE'
    if connectivity_check(graph_adj, v, e) > 1:
        return 'NONE'
    if not even_degree_nodes(graph_adj):
        return 'NONE'

    node = 0
    S = [node]
    result = []
    while S:
        if graph_adj[S[-1]]:
            current_node = S[-1]
            highest_degree_node = None
            for idx, i in enumerate(graph_adj[S[-1]]):
                if len(graph_adj[i]) < degree:
                    degree = len(graph_adj[i])
                    highest_degree_node = idx
            # select node to move next
            adj_node = graph_adj[ S[-1] ][highest_degree_node]
            S.append(adj_node)
            # Mark as visited edge between two nodes
            graph_adj[current_node].remove(adj_node)
            graph_adj[adj_node].remove(current_node)
        else:
            last_node = S.pop()
            result.append(last_node)

        return [i+1 for i in result[:-1]]

answer = eulers_cycle(graph_adj, v, e)
if answer == 'NONE':
    print(answer)
else:
    for i in answer:
        print(i, end=' ')
