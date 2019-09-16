from igraph import Graph, Vertex
from typing import List, Union, Tuple


def remove_vertex_if_contained_neighbors(graph: Graph):
    to_remove_set = set()
    v: Vertex
    for v in graph.vs:
        u: Vertex
        for u in v.neighbors():
            u_neighbors = set(u.neighbors())
            u_neighbors.remove(v)
            if set(v.neighbors()).issuperset(u_neighbors):
                to_remove_set.add(v)

    add_to_cover_list = [v['name'] for v in to_remove_set]

    graph.delete_vertices(to_remove_set)
    return add_to_cover_list
