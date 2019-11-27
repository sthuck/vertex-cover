from typing import List, Union, Tuple

import scipy
import scipy.sparse as sp
from igraph import Graph, Vertex

from algorithms.reductions import reduce_graph, print_graph_info
from graph_utils import set_name


def find_first_vertex_with_degree(graph: Graph) -> Union[int, None]:
    v: Vertex
    for v in graph.vs:
        if v.degree() > 0:
            return v.index

    return None


def compute_x(v: Vertex):
    deg = v.degree()
    return deg / (deg + 1)


def compute_x_minus_1(v: Vertex):
    deg = v.degree()
    return (deg - 1) / deg


def compute_y(v: Vertex):
    return sum([compute_x(n) for n in v.neighbors()]) + compute_x(v)


def compute_z(v: Vertex):
    return sum([compute_x_minus_1(n) for n in v.neighbors()]) + 1


def xyz_weak_select_vertex(graph: Graph) -> Union[Tuple[List[int], List[int]], None]:

    v_index = find_first_vertex_with_degree(graph)
    if v_index is None:
        return None
    v: Vertex = graph.vs[v_index]

    y = compute_y(v)
    z = compute_z(v)

    if z - y <= 0:

        return [v_index], []
    else:
        return [n.index for n in v.neighbors()], [v_index]


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def zero_vertices_by_index(graph: Graph, vertex: Union[int, List[int]]):
    graph.delete_vertices(vertex)


def build_sparse(graph: Graph):
    return scipy.sparse.csr_matrix(graph.get_adjacency().data)


def print_vertex_number(graph: Graph):
    print(f'vertex number: {len([v for v in graph.vs if v.degree() > 0])}')


def xyz_weak_algo(_, orig: Graph):
    log = False
    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    removed_counter = 0
    iteration = 0

    if log:
        print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='xyz_weak: start')
        print_vertex_number(graph)

    while True:

        add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=True)
        cover_group.extend(add_to_cover)
        removed_counter += removed_in_reduce

        # xyz
        result = xyz_weak_select_vertex(graph)
        if result is None:
            break

        add_to_cover_index, to_remove_index = result

        if log:
            print(f'will be added to cover: {[graph.vs[i]["name"] for i in add_to_cover_index]}')
            print(f'will be removed (not in cover): {[graph.vs[i]["name"] for i in to_remove_index]}')

        cover_group = cover_group + [graph.vs[i]['name'] for i in add_to_cover_index]
        zero_vertices_by_index(graph, add_to_cover_index + to_remove_index)

        iteration += 1
        if log:
            print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True,
                             label=f'xyz_weak: iteration ${iteration}')
            print_vertex_number(graph)

    return list(cover_group), removed_counter
