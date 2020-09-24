'''
An implementation of the depth-first search algorithm
But actually this script calculates the number of components in the graph using 
depth-first search
ALGORITHM DESCRIPTION
1) Visit the vertex x;
2) Mark it as visited;
3) Move to some adjacent vertex of x;
4) Repeat the same 1, 2 steps

This program take input from input()
For example,
3 3 - no. of vertices, no. of edges;
next lines are edges
1 2
2 3
3 1
'''

# v - no. of vertices; e - no. of edges -- first line input
v, e = map(int, input().split())
# creates adjacency dictionary for the graph
graph_adj = {i:[] for i in range(v)}

for i in range(e):
     v1, v2 = map(int, input().split()) # all consequent lines of input
     graph_adj[v1 - 1].append(v2-1)
     graph_adj[v2 - 1].append(v1-1)

def depth_first_search(graph_adj, current_vertex, visited_vertices):
    '''graph_adj - adjacency list; current_vertex - the vertex neighbor of which will
    be checked; visited - a set of vertices that have been visited
    '''
    visited_vertices.add(current_vertex)
    if graph_adj[current_vertex]:
        # visit adjacent vertices that are not visited
        for i in set(graph_adj[current_vertex]) - visited_vertices:
            depth_first_search(graph_adj, i, visited_vertices)
        return visited_vertices

def graph_components(graph_adj):
    ''' Counts the number of components in the graph - subgraphs that
    are not connected with each other
    '''
    visited_vertices = set()
    vertices = set(i for i in graph_adj.keys())
    num_components = 0
    while vertices:
        next_vertex = next(iter(vertices))
        # when vertex does not have incident edges -->
        # this vertex -  separate component in the graph
        if not graph_adj[next_vertex]:
            vertices.remove(next_vertex)
            num_components += 1
        else:
            visited_vertices = depth_first_search(graph_adj,
                                next_vertex, visited_vertices)
            num_components += 1
        if visited_vertices:
            vertices -= visited_vertices
    return num_components

print(graph_components(graph_adj))


euler_cycle = [0] # this wil be the sequence of node in the euler's cycle;
# as you can see, it always start with 0 node. But algorithm will work for
# any starting node

def remove_free_nodes(graph_adj):
    ''' Given the adjcency dictionary for the graph, removes
    all vertices without incident vertices
    '''
    free_nodes = [node for node, edges in graph_adj.items() if edges==[]]
    for n in free_nodes: # remove all nodes that does not have edges
        if not graph_adj[n]:
            del graph_adj[n]
    return graph_adj

def even_degree_nodes(graph_adj):
    ''' Checks whether all  vertices have the even number
    of edges - a requirement for euler's cycle in the graph
    '''
    for i in graph_adj.values():
        if len(i) % 2 != 0 and len(i) != 0:
            return False
    return True

def find_euler_cycle(graph_adj, v, e):
    ''' Returns one of the many possible euler's cycles in the graph
    '''
    if e == 0:
        return 'NONE'
    if graph_components(graph_adj) > 1:
        return 'NONE'
    if not even_degree_nodes(graph_adj):
        return 'NONE'
    while len(euler_cycle) < e: # whil
        node = euler_cycle[-1]
        graph_adj = remove_free_nodes(graph_adj)
        if graph_adj[node]: # if it has adjacent nodes
            # choose next point based on whether the removal 
            # of an edge will change the no. of components in the graph to > 1
            for n in graph_adj[node]:
                graph_adj[node].remove(n)
                graph_adj[n].remove(node)
                if graph_components(graph_adj) == 1:
                    euler_cycle.append(n)
                    break
                else:
                    # if removal changes no. of comp, then add edges back
                    graph_adj[node].append(n)
                    graph_adj[n].append(node)
    return [i+1 for i in euler_cycle]

answer = find_euler_cycle(graph_adj, v, e)
if answer == 'NONE':
    print(answer)
else:
    for i in answer:
        print(i, end=' ')





