from igraph import Graph, Vertex
from typing import List, Union, Tuple


def find_parents_of_leaves(graph: Graph):
    all_leaves = [v for v in graph.vs if v.degree() == 1]
    parents = {leaf.neighbors()[0] for leaf in all_leaves}
    return parents


def remove_parents_of_leaves(graph: Graph) -> List[int]:
    add_to_cover = []
    while True:
        parents = find_parents_of_leaves(graph)
        if len(parents) == 0:
            break
        add_to_cover.extend([v['name'] for v in parents])
        graph.delete_vertices(parents)

    return add_to_cover