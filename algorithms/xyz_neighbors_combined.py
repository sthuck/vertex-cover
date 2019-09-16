from igraph import Graph, Vertex, Matrix
from typing import List, Tuple
import scipy.sparse as sp
import numpy

from algorithms.neighbors_algo import compute_t
from algorithms.xyz.xyz_common_code import get_x_vector, get_y_vector, get_z_vector
from algorithms.xyz.xyz_utils import all_vertex_degree
from graph_utils import set_name


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def convert_graph_to_sparse(graph: Graph):
    m = graph.get_adjacency()
    return sp.csr_matrix(m.data)


# def compute_xyz_diff_vector(sparse: sp.csr_matrix):
#     vertex_degree_vector = all_vertex_degree(sparse)
#
#     x_vector = get_x_vector(vertex_degree_vector)
#     y_vector: numpy.ndarray = get_y_vector(sparse, x_vector)
#     z_vector: numpy.ndarray = get_z_vector(sparse, vertex_degree_vector)
#     return (z_vector - y_vector).tolist()[0]

def compute_k(graph: Graph, vertex: Vertex):
    neighbors = vertex.neighbors()
    sum_x = 0
    for v in graph.vs:
        if v == vertex:
            pass
        elif v in neighbors:
            x = (v.degree() - 1) / v.degree()
            sum_x = sum_x + x
        else:
            sum_x = sum_x + (v.degree() / (v.degree() + 1))

    return sum_x + 1


# In return_value[0] returns the vertices to add to cover
# in return_value[1] any other vertices we wish to remove without adding
def select_vertices(graph: Graph) -> Tuple[List[int], List[int]]:
    t_values = [(v.index, compute_t(graph, v)) for v in graph.vs]
    k_values = [(v.index, compute_k(graph, v)) for v in graph.vs]
    # zy_diff_vector = [pair for pair in enumerate(compute_xyz_diff_vector(convert_graph_to_sparse(graph)))]

    lowest_t_index, lowest_t_value = min(t_values, key=lambda item: item[1])
    lowest_k_index, lowest_k_value = min(k_values, key=lambda item: item[1])

    if lowest_t_value > lowest_k_value:
        lowest_k_vertex = graph.vs[lowest_k_index]
        return [lowest_k_vertex['name']], []
    else:
        lowest_t_vertex = graph.vs[lowest_t_index]
        return [v['name'] for v in lowest_t_vertex.neighbors()], [lowest_t_vertex['name']]


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def find_parents_of_leaves(graph: Graph):
    all_leaves = [v for v in graph.vs if v.degree() == 1]
    parents = {leaf.neighbors()[0] for leaf in all_leaves}
    return [parent['name'] for parent in parents]


def xyz_neighbors_combined_algo(_, orig: Graph):
    cover_group = []
    graph: Graph = orig.copy()
    set_name(graph)

    while not is_empty_graph(graph):
        parents = find_parents_of_leaves(graph)
        zero_vertices(graph, parents)
        cover_group = cover_group + parents

        if is_empty_graph(graph):
            break

        selected_vertices, vertices_to_zero = select_vertices(graph)
        zero_vertices(graph, selected_vertices + vertices_to_zero)
        cover_group = cover_group + selected_vertices
    return cover_group
