import numpy as np
import scipy.sparse as sp
import scipy
from .xyz_utils import all_vertex_degree, build_sparse, zero_vertex, is_empty_graph
from .xyz_common_code import get_x_vector, get_y_vector, get_z_vector


def xyz_select_vertex(graph: sp.lil_matrix):
    sparse = graph.tocsr()

    if is_empty_graph(sparse):
        return None

    vertex_degree_vector = all_vertex_degree(sparse)

    x_vector = get_x_vector(vertex_degree_vector)
    y_vector = get_y_vector(sparse, x_vector)
    z_vector = get_z_vector(sparse, vertex_degree_vector)

    diff_vector = z_vector - y_vector
    return diff_vector.argmin()


def get_all_leaves(graph: sp.lil_matrix):
    degree_vertex = all_vertex_degree(graph)
    leaves = np.where(degree_vertex == 1)[0]
    return leaves


def get_parent_of_leaf(graph: sp.lil_matrix, leaf_index: int):
    # graph[leaf_index] returns matrix of one column, so np.nonzero also returns matrix
    possible_parent = np.nonzero(graph[leaf_index])[1]

    return possible_parent[0] if len(possible_parent) == 1 else None


def xyz_v2_algo(graph: np.ndarray, *args):
    sparse = build_sparse(graph)
    cover_group = set()

    while True:
        while True:
            leaves = get_all_leaves(sparse)
            if len(leaves) == 0:
                break
            parents = map(lambda vertex_index: get_parent_of_leaf(sparse, vertex_index), leaves)
            for parent in parents:
                if parent is not None:
                    zero_vertex(sparse, parent)
                    cover_group.add(parent)

        selected_vertex = xyz_select_vertex(sparse)
        if selected_vertex is None:
            break
        zero_vertex(sparse, selected_vertex)
        cover_group.add(selected_vertex)
    return list(cover_group)
