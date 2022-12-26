from igraph import Graph, Vertex
import random
from typing import Set, List
import heapq


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

    v_values_dict = {v.index: 0 for v in graph.vs} # initial, just for initial compute_v_value call

    def compute_v_value(v: Vertex):
        Nv = {v}.union(v.neighbors())
        W = {v for v in graph.vs if v.index in v_values_dict}
        W_tag = W.intersection(Nv)
        return len(W_tag)

    # key - vertex index, value: v_value
    # dict without vertices in B, or neighbors of B == W
    v_values_dict = {v.index: compute_v_value(v) for v in graph.vs}
    v_values = [(v_value, index) for (index, v_value) in v_values_dict.items()]
    heapq.heapify(v_values)

    while b > 0:
        v_value, chosen_v_index = v_values[0]
        chosen_v = graph.vs[chosen_v_index]
        B.add(chosen_v)
        chosen_v_neighbors = set(chosen_v.neighbors())
        chose_v_neighbors_neighbors = [v.neighbors() for v in chosen_v_neighbors if v not in chosen_v_neighbors]

        v_values_dict.pop(chosen_v.index)

        for vn in chosen_v_neighbors:  # remove v_neighbors from v_values
            if vn.index in v_values_dict: v_values_dict.pop(vn.index)

        for vnn in chose_v_neighbors_neighbors:  # update v_neighbors_of_neighbors in v_values
            v_values_dict[vnn.index] = compute_v_value(vnn)

        v_values = [(v_value, index) for (index, v_value) in v_values_dict.items()]
        heapq.heapify(v_values)

        b -= 1
    W = set(v for v in graph.vs if v.index in v_values_dict)
    return graph, W


## old v1 implementaion

# def bwc_min_algo(graph: Graph, initial_b: int):
#     b = initial_b
#     v: Vertex
#     B: Set[Vertex] = set()
#     B_neighbors: Set[Vertex] = set()
#
#     def compute_v_value(v: Vertex):
#         B_tag = B.union([v])
#         B_neighbors_tag = B_neighbors.union(v.neighbors())
#         W_tag = [v for v in graph.vs if v not in B_tag and v not in B_neighbors_tag]
#         return len(W_tag)
#
#     while b > 0:
#         v_candidates = [v for v in graph.vs if v not in B]
#         v_values = [(v, compute_v_value(v)) for v in v_candidates]
#         chosen_v = max(v_values, key=lambda x: x[1])[0]
#         B.add(chosen_v)
#         B_neighbors = B_neighbors.union(chosen_v.neighbors())
#         b -= 1
#
#     W = set(v for v in graph.vs if v not in B_neighbors and v not in B)
#
#     return graph, W
