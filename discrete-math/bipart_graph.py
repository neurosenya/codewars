from collections import OrderedDict
from collections import deque

v, e = map(int, input().split())
graph_adj = {i:[] for i in range(v)}

for i in range(e):
    v1, v2 = map(int, input().split())
    graph_adj[v1-1].append(v2-1)
    graph_adj[v2-1].append(v1-1)

#print(graph_adj)

q = deque()
visited = [False for i in range(v)]
for key, value in graph_adj.items():
    if value:
        q.append(key)
        visited[key] = True
        break

result = OrderedDict({key: 0 for key in range(v)})

while False in visited:
    if not q:
        for key, value in graph_adj.items():
            if not visited[key]:
                q.append(key)
                visited[key] = True
                break
    ver = q.popleft()
    for v in graph_adj[ver]:
        if visited[v] == False:
            q.append(v)
            result[v] = result[ver] + 1
            visited[v] = True

#print(result)
#print(graph_adj)
def evaluate(graph_adj, result):
    for key, value in graph_adj.items():
        for i in value:
            if result[key] % 2 == result[i] % 2:
                return 'NO'
    return 'YES'

print(evaluate(graph_adj, result))
