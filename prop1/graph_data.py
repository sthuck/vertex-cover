from igraph import Graph, Vertex, Edge
import numpy as np


def dv_divide_dv_1_squared(graph: Graph):
    def helper(v: Vertex):
        dv = v.degree()
        dv_1_squared = (dv + 1) ** 2
        return dv / dv_1_squared

    return np.array([helper(v) for v in graph.vs]).sum()


def neighbors_1_divide_dv(graph: Graph):
    def helper(e: Edge):
        dv_1 = graph.vs[e.target].degree() + 1
        dv_2 = graph.vs[e.source].degree() + 1
        return 1 / (dv_1 * dv_2)

    return np.array([helper(e) for e in graph.es]).sum()


def find_common_neighbors(graph: Graph, v_index_1: int, v_index_2: int):
    v1 = graph.vs[v_index_1]
    v2 = graph.vs[v_index_2]
    n1 = set(v1.neighbors())
    return len(n1.intersection(v2.neighbors()))


def find_all_non_neighbors(graph: Graph):
    comp = graph.complementer()
    return [(e.source, e.target) for e in comp.es]


def compute_third_thing_shaked_find_a_better_name(graph: Graph):
    all_non_neighbors = find_all_non_neighbors(graph)

    def helper(v1: int, v2: int):
        mij = find_common_neighbors(graph, v1, v2)
        dv1 = graph.vs[v1].degree()
        dv2 = graph.vs[v2].degree()
        return mij / ((dv1 + 1) * (dv2 + 1) * (dv1 + dv2 + 2 - mij))

    return np.array([helper(v1, v2) for (v1, v2) in all_non_neighbors]).sum()


def formula_prop_1(graph: Graph):
    return dv_divide_dv_1_squared(graph) - 2 * neighbors_1_divide_dv(graph) + 2 * compute_third_thing_shaked_find_a_better_name(graph)