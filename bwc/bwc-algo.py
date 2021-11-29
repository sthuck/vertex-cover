from igraph import Graph, Vertex
from typing import Set
import numpy as np
import pandas as pd
from enum import Enum
import random

# function compute E_w(G, C, selcted_vertex):
#  G2 = G.copy()
#  remove selectd_vertex from G2
#  C2 = C union N(selected_vertex)
#  sum over v in (G.vs - C):

def computeE_w_helper(degree, n, b):
    numerator = np.prod([(n-(degree + i)) for i in range(1, b+1)])
    denumerator =  np.prod([(n-i) for i in range(0, b+2)])
    return numerator/denumerator


def computeE_w(selected_vertex: Vertex, graph: Graph, C: Set[int], b: int) -> float:
    copy: Graph = graph.copy()
    C2 = C.union([n['orig_index'] for n in selected_vertex.neighbors()])
    copy.delete_vertices(selected_vertex.index)
    return sum([computeE_w_helper(v.degree(), len(copy.vs), b) for v in copy.vs if v['orig_index'] not in C2])


def main():
    n = 1000
    c = 0.5
    p = c / n
    initial_b = 10
    graph: Graph = Graph.Erdos_Renyi(n=n, p=p)

    b = initial_b
    C = set()
    v: Vertex

    for v in graph.vs:
        v['orig_index'] = v.index

    while b > 0:
        print(f'b={b}')
        E_w_vector = [(v, computeE_w(v, graph, C, b)) for v in graph.vs if v['orig_index'] not in C]
        max_Ew_vertex = max(E_w_vector, key=lambda x: x[1])[0]
        C = C.union(n['orig_index'] for n in max_Ew_vertex.neighbors())
        C = C - {max_Ew_vertex['orig_index']}
        graph.delete_vertices(max_Ew_vertex.index)
        b = b - 1

    print(f'n={len(graph.vs)}')
    print(f'C = {len(C)}')
    print(f'w = {len(graph.vs) - len(C)}')


if __name__ == '__main__':
    main()

# g = G(n, p)
# initial_b=b <= input
# B = {} // at the end |B| should be b
# output w: |W={group of veritices|
# W = {}
# while B not empty:
# iterate until |B| = initial_b or b = 0
#  for each v in g.vs:
#      compute E_w for vertices not in C => in other words, E_w is a function E_w(v, C): number
#   max_v = select v where E_w(v) is maximal
#   add max_v to B
#   delete all edges of max_v => delete max_v from graph
#   C = C union {neighbors of max_v}
#   // now n = n - 1
#   // b = b - 1

# function compute E_w(G, C, selcted_vertex):
#  G2 = G.copy()
#  remove selectd_vertex from G2
#  C2 = C union N(selected_vertex)
#  sum over v in (G.vs - C):
