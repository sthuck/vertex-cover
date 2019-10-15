from igraph import Graph, Vertex
from typing import List, Tuple

from graph_utils import set_name
import random
from functools import reduce
from algorithms.reductions import reduce_graph


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def compare_vertices(v1: Vertex, v2: Vertex):
    v1d = v1.degree()
    v2d = v2.degree()
    if v1d < v2d:
        return v1
    elif v1d > v2d:
        return v2
    else:
        n: Vertex
        sum_neighbours_degree_v1 = sum([n.degree() for n in v1.neighbors()])
        sum_neighbours_degree_v2 = sum([n.degree() for n in v2.neighbors()])
        if sum_neighbours_degree_v1 > sum_neighbours_degree_v2:
            return v1
        elif sum_neighbours_degree_v1 < sum_neighbours_degree_v2:
            return v2
        else:
            random_number = random.randint(0, 1)
            return v1 if random_number == 0 else v2


def select_vertices(graph: Graph) -> List[str]:
    selected_vertex = reduce(compare_vertices, [v for v in graph.vs if v.degree() > 0])
    return [n['name'] for n in selected_vertex.neighbors()]


def zero_vertices(graph: Graph, selected_vertices: List[str]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def novac1_algo(_, orig: Graph):
    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    removed_counter = 0

    while not is_empty_graph(graph):

        add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=True)
        cover_group.extend(add_to_cover)
        removed_counter += removed_in_reduce

        if is_empty_graph(graph):
            break
        selected_vertices = select_vertices(graph)
        zero_vertices(graph, selected_vertices)
        cover_group = cover_group + selected_vertices

    return cover_group, removed_counter
