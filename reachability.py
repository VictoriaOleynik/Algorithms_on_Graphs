#Uses python3
import sys
def reach(x, y):
    explore(x)
    if visited[y]==1:
        return 1
    else:
        return 0

def explore(v):
    visited[v]=1
    for w in adj[v]:
        if visited[int(w)]==0:
            explore(w)
    return

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    visited=[0 for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(x,y))



