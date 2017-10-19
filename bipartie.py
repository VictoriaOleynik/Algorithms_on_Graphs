#Uses python3

import sys
import queue

def bipartite(adj):
    while Q.empty()!=1:
        u = Q.get()
        for v in adj[u]:
            if colors[v]==0:
                Q.put(v)
                colors[v]=colors[u]*(-1)
            else:
                if colors[u]==colors[v]:
                    return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    colors =  [0 for _ in range(n)]
    Q = queue.Queue()
    Q.put(0)
    colors[0]=1
    print(bipartite(adj))
