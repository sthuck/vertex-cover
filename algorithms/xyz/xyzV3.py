import numpy as np
import scipy.sparse as sp
import scipy

from graph_utils import set_name
from .xyz_utils import all_vertex_degree, is_empty_graph as is_empty_graph_sparse
from .xyz_common_code import get_x_vector, get_y_vector, get_z_vector
from algorithms.reductions import reduce_graph, ReductionCounters
from igraph import Graph, Vertex
from typing import List, Union, Tuple
import random


def find_minimum(arr: np.ndarray, vertex_degree_vector):
    minimum = float("inf")
    minimum_index = []
    for index, num in enumerate(arr):
        if vertex_degree_vector[index] == 0:
            continue  # don't pick 0 degree vertices

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

    vertex_degree_vector = all_vertex_degree(sparse)  # vector of all degrees per vertex

    x_vector = get_x_vector(vertex_degree_vector)  # vector of, for v in V, d(v)/d(v)+1
    y_vector = get_y_vector(sparse, x_vector)
    z_vector = get_z_vector(sparse, vertex_degree_vector)

    diff_vector = z_vector - y_vector
    selected_index = find_minimum(diff_vector, vertex_degree_vector)

    return selected_index


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def zero_vertices_by_index(graph: Graph, vertex: Union[int, List[int]]):
    graph.delete_vertices(vertex)


def build_sparse(graph: Graph):
    return scipy.sparse.csr_matrix(graph.get_adjacency().data)


def xyz_v3_algo(_, orig: Graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=False):
    return _xyz_v3_algo_base(_, orig, do_reduce_1, do_reduce_2, do_reduce_3)


def xyz_v3_algo_with_reductions(_, orig: Graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=False):
    return _xyz_v3_algo_base(_, orig, do_reduce_1=do_reduce_1, do_reduce_2=do_reduce_2,
                                                   do_reduce_3=do_reduce_3)


def _xyz_v3_algo_base(_, orig: Graph, do_reduce_1=False, do_reduce_2=False, do_reduce_3=False):
    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    removed_counter = 0
    reduction_counters = ReductionCounters()  # for tracking reductions

    add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=do_reduce_1, do_reduce_2=do_reduce_2,
                                                   do_reduce_3=do_reduce_3, counters=reduction_counters)
    removed_in_first_reduction_first_iteration = reduction_counters.reduction_1_counter

    cover_group.extend(add_to_cover)
    removed_counter += removed_in_reduce

    while True:

        add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=do_reduce_1, do_reduce_2=do_reduce_2,
                                                       do_reduce_3=do_reduce_3, counters=reduction_counters)
        cover_group.extend(add_to_cover)
        removed_counter += removed_in_reduce

        # xyz
        selected_vertex_index = xyz_select_vertex(graph)
        if selected_vertex_index is None:
            break
        cover_group.append(graph.vs[selected_vertex_index]['name'])
        zero_vertices_by_index(graph, selected_vertex_index)
    return list(cover_group), removed_counter, \
           {'removed_in_first_reduction_first_iteration': removed_in_first_reduction_first_iteration,
            'reduction_counters': reduction_counters}
