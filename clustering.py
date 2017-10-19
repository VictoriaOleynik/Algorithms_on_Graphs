#Uses python3
import sys
import math
import itertools

parent = dict()
rank = dict()


def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
                parent[root2] = root1
        else:
            parent[root1] = root2
    if rank[root1] == rank[root2]: rank[root2] += 1


def kruskal(graph, k):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
        #print edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        cc = [find(vertice) for vertice in graph['vertices']]
        num_cc=len(set(cc))
        d = edge[0]
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
        cc = [find(vertice) for vertice in graph['vertices']]
        num_cc_new=len(set(cc))
        if num_cc == k and num_cc_new < k:
            return(d)
    return (d)


def clustering(x, y, k):
    #write your code here
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    points = list(zip(x,y))
    n=len(points)
    points_ind = [(i, points[i]) for i in range(n)]
    edges = list(itertools.combinations(points_ind, 2))
    V = set(range(n))
    edges = [(math.sqrt((edges[i][0][1][0]-edges[i][1][1][0])**2+(edges[i][0][1][1]-edges[i][1][1][1])**2),edges[i][0][0],edges[i][1][0]) for i in range(len(edges))]
    edges = set(edges)
    graph = {
        'vertices': V,
        'edges': edges
            }
    print("{0:.9f}".format(kruskal(graph, k)))