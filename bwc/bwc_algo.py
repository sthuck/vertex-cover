from igraph import Graph, Vertex
from typing import Set
import numpy as np
import pandas as pd
from enum import Enum
import random
from king_graph import rook_graph, king_graph

# function compute E_w(G, C, selcted_vertex):
#  G2 = G.copy()
#  remove selectd_vertex from G2
#  C2 = C union N(selected_vertex)
#  sum over v in (G.vs - C):

def computeE_w_helper(degree, n, b):
    numeratorSet = set([(n-(degree + i)) for i in range(1, b+1)])
    denumSet = set([(n-i) for i in range(0, b)]) #0 to b-1
    inBoth = numeratorSet.intersection(denumSet)
    numeratorV = np.array(list(numeratorSet - inBoth)).astype(np.float64)
    denumeratorV = np.array(list(denumSet - inBoth)).astype(np.float64)

    numerator = np.prod(numeratorV) # [3,4,10]
    denumerator = np.prod(denumeratorV)
    return numerator/denumerator


def computeE_w(selected_vertex: Vertex, graph: Graph, C: Set[int], b: int) -> float:
    copy: Graph = graph.copy()
    C2 = C.union([neighbor['orig_index'] for neighbor in selected_vertex.neighbors()])
    copy.delete_vertices(selected_vertex.index)
    if b == 1:
        new_N = len(copy.vs)
        return new_N - len(C2)
    else:
        return sum([computeE_w_helper(v.degree(), len(copy.vs), b-1) for v in copy.vs if v['orig_index'] not in C2])


def bwc_algo(graph: Graph, initial_b):
    b = initial_b
    C = set()
    v: Vertex

    for v in graph.vs:
        v['orig_index'] = v.index

    while b > 0:
        print(f'b={b}')
        E_w_vector = [(v, computeE_w(v, graph, C, b)) for v in graph.vs]
        max_Ew_vertex = max(E_w_vector, key=lambda x: x[1])[0]
        C = C.union(n['orig_index'] for n in max_Ew_vertex.neighbors())
        C = C - {max_Ew_vertex['orig_index']}
        graph.delete_vertices(max_Ew_vertex.index)
        b = b - 1
    return graph, C

def main():
    n = 1000
    c = 1
    p = c / n
    initial_b = 10
    graph: Graph = Graph.Erdos_Renyi(n=n, p=p)
    # graph = king_graph(n=10, m=10)
    graph = rook_graph(n=6, m=9)


    graph, C = bwc_algo(graph, initial_b)

    print(f'n={len(graph.vs)}')
    print(f'C = {len(C)}')
    print(f'w = {len(graph.vs) - len(C)}')



if __name__ == '__main__':
    main()

# g = G(n, p)
# initial_b=b <= input
# B = {} // at the end |B| should be b
# output w: |W={group of vertices|
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
#  remove selected_vertex from G2
#  C2 = C union N(selected_vertex)
#  sum over v in (G.vs - C):

