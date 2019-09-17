from igraph import Graph, Vertex
from typing import List, Union, Tuple

from algorithms.reductions.print_info import print_graph_info


def find_parents_of_leaves(graph: Graph):
    all_leaves = [v for v in graph.vs if v.degree() == 1]
    parents = {leaf.neighbors()[0] for leaf in all_leaves}
    return parents


def remove_parents_of_leaves(graph: Graph, one_time=False, log=False) -> List[str]:
    add_to_cover = []
    iteration = 0
    while True:
        iteration += 1
        parents = find_parents_of_leaves(graph)
        if log:
            print(f'before iteration: {iteration}, found {len(parents)} parents of leaves')

        if len(parents) == 0:
            break
        add_to_cover.extend([v['name'] for v in parents])
        graph.delete_vertices(parents)

        if log:
            print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label=f'after iteration {iteration}')

        if one_time:
            break

    return add_to_cover
