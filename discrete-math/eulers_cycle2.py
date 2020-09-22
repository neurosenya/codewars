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
graph_adj = {i:[] for i in range(v)}

for i in range(e):
     v1, v2 = map(int, input().split())
     graph_adj[v1 - 1].append(v2-1)
     graph_adj[v2 - 1].append(v1-1)

def depth_first_search(graph, current_vertex, visited):
    # mark vertex as visited
    visited.add(current_vertex)
    if graph[current_vertex]:
        for i in set(graph[current_vertex]) - visited: # it will only visit adjacent vertices that are not visited yet
            depth_first_search(graph, i, visited)
        return visited

print(graph_adj)
def graph_components(graph_adj):
    num_components = 0
    visited_vertices = set()
    vertices = set(i for i in graph_adj.keys())
    print(vertices)
    num_components = 0
    while len(vertices) > 1:
        if not visited_vertices and num_components > 0:
            num_components += len(vertices)-1
            break
        visited_vertices = depth_first_search(graph_adj, next(iter(vertices)), visited_vertices)
        num_components += 1
        if visited_vertices:
            vertices -= visited_vertices

    return num_components
print(graph_components(graph_adj))

# The actual algorithm for finding the euler's cycle
euler_cycle = [0]
def remove_free_nodes(graph_adj):
    free_nodes = [node for node, edges in graph_adj.items() if edges==[]]
    for n in free_nodes: # remove all nodes that does not have edges
        if not graph_adj[n]:
            del graph_adj[n]
    return graph_adj


def add_back_free_nodes(graph_adj):
    free_nodes = [node for node, edges in graph_adj.items() if edges==[]]
    for n in free_nodes: # remove all nodes that does not have edges
        graph_adj[n] = []
    return graph_adj


while len(euler_cycle) < e: # whil
    node = euler_cycle[-1]
    graph_adj = remove_free_nodes(graph_adj)
    print(graph_adj, euler_cycle)
    if graph_adj[node]: # if it has adjacent nodes
        # choose next point based on whether the removal of an edge will increase the no. of components in the graph
        for n in graph_adj[node]:
            graph_adj[node].remove(n)
            graph_adj[n].remove(node)
            graph_adj = remove_free_nodes(graph_adj)
            if graph_components(graph_adj) == 1:
                print(euler_cycle)
                print(graph_adj)
                euler_cycle.append(n)
                break
            else:
                graph_adj = add_back_free_nodes(graph_adj)
                graph_adj[node].append(n)
                graph_adj[n].append(node)

print([i for i in euler_cycle])







