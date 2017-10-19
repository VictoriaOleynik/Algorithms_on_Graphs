#Uses python3
import sys
import math
#from scipy.spatial import distance
from heapq import heappop, heappush, heapify
import itertools


def make_queue(v, cost):
    h = []
    for u in v:
        heappush(h,((cost[u], u)))
    heapify(h)
    return h


def change_priority(h, v, dist_v, old_dist):
    h.remove((old_dist, v))
    heappush(h,(dist_v, v))
    heapify(h)
    return h


def minimum_distance(x, y):
    points = list(zip(x,y))
    n=len(points)
    points_ind = [(i, points[i]) for i in range(n)]
    edges = list(itertools.permutations(points_ind, 2))
    edges = [((edges[i][0][0],edges[i][1][0]), math.sqrt((edges[i][0][1][0]-edges[i][1][1][0])**2+(edges[i][0][1][1]-edges[i][1][1][1])**2)) for i in range(len(edges))]

    weights = [[] for _ in range(n)]
    adj = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a].append(b)
        weights[a].append(w)

    n = len(points)
    V = range(n)
    cost = [[] for _ in range(n)]
    parent = [[] for _ in range(n)]

    for u in V:
        cost[u] = sys.maxsize
        parent[u] = None
    u0 = 0
    cost[u0] = 0

    h = make_queue(V, cost)
    while h:
        v_vertex = heappop(h)
        v = v_vertex[1]
        for i in range(len(adj[v])):
            z = adj[v][i]
            if (cost[z],z) in h and cost[z] > weights[v][i]:
                old_cost=cost[z]
                cost[z] = weights[v][i]
                parent[z] = v
                change_priority(h,z,cost[z],old_cost)
    result = sum(cost)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
