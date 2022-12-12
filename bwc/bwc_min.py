from igraph import Graph, Vertex
import random
from typing import Set, List


# given graph G, b = number of needed blacks
# W =  ()
# B = ()
# B_neighbors = ()

# while b > 0
#   for each vertex v not in B already:
#     compute B_tag = B union v
#     compute B_neighbors_tag = B_neighbors union v.neighbors()
#     compute W_Tag = graph.vs - B_tag - B_neighbors_tag
#     compute v_value = len(W_Tag)
#   choose v with maximal v_value -> B = B union chosen v
#   B_neighbors = B_neighbors union v.neighbors()
#   b = b - 1


def bwc_min_algo(graph: Graph, initial_b: int):
    b = initial_b
    v: Vertex
    B: Set[Vertex] = set()
    B_neighbors: Set[Vertex] = set()

    def compute_v_value(v: Vertex):
        B_tag = B.union([v])
        B_neighbors_tag = B_neighbors.union(v.neighbors())
        W_tag = [v for v in graph.vs if v not in B_tag and v not in B_neighbors_tag]
        return len(W_tag)

    while b > 0:
        v_candidates = [v for v in graph.vs if v not in B]
        v_values = [(v, compute_v_value(v)) for v in v_candidates]
        chosen_v = max(v_values, key=lambda x: x[1])[0]
        B.add(chosen_v)
        B_neighbors = B_neighbors.union(chosen_v.neighbors())
        b -= 1

    W = set(v for v in graph.vs if v not in B_neighbors and v not in B)

    return graph, W
