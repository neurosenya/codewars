## Depth first-search
 Implemented using stack, which keeps track of all the visited nodes. 

- Visit a vertex *s*
- mark *s* as visited
- Recursively visit each vertex attached to *s*

A recursive imlementations of DFS:

```
DFS(G, v):
    label v as discivered
    for w in  G.adhacentEdges(v):
        if vertex w is not labeled as discovered:
            DFS(G, w)
```
