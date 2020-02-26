import numpy as np
import scipy.sparse as sp
import scipy

from graph_utils import set_name
from .xyz_utils import all_vertex_degree, is_empty_graph as is_empty_graph_sparse
from .xyz_common_code import get_x_vector, get_y_vector, get_z_vector
from algorithms.reductions import reduce_graph
from igraph import Graph, Vertex
from typing import List, Union, Tuple
import random


def find_minimum(arr: np.ndarray):
    minimum = float("inf")
    minimum_index = []
    for index, num in enumerate(arr):
        if num == minimum:
            minimum_index += [index]
        elif num > minimum:
            continue
        elif num < minimum:
            minimum = num
            minimum_index = [index]

    select_random_index = random.randint(0, len(minimum_index) - 1)
    return minimum_index[select_random_index]


def xyz_select_vertex(graph: Graph) -> Union[int, None]:
    sparse = build_sparse(graph)

    if is_empty_graph_sparse(sparse):
        return None

    vertex_degree_vector = all_vertex_degree(sparse)

    x_vector = get_x_vector(vertex_degree_vector)
    y_vector = get_y_vector(sparse, x_vector)
    z_vector = get_z_vector(sparse, vertex_degree_vector)

    diff_vector = z_vector - y_vector
    return find_minimum(diff_vector)


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def zero_vertices_by_index(graph: Graph, vertex: Union[int, List[int]]):
    graph.delete_vertices(vertex)


def build_sparse(graph: Graph):
    return scipy.sparse.csr_matrix(graph.get_adjacency().data)


def xyz_v3_algo(_, orig: Graph):
    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    removed_counter = 0

    # add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=True)
    # cover_group.extend(add_to_cover)
    # removed_counter += removed_in_reduce

    while True:

        add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=False)
        cover_group.extend(add_to_cover)
        removed_counter += removed_in_reduce

        # xyz
        selected_vertex_index = xyz_select_vertex(graph)
        if selected_vertex_index is None:
            break
        cover_group.append(graph.vs[selected_vertex_index]['name'])
        zero_vertices_by_index(graph, selected_vertex_index)
    return list(cover_group), removed_counter
