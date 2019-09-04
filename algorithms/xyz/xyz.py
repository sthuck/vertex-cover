import numpy as np
import scipy.sparse as sp
import scipy
from .xyz_utils import build_sparse, zero_vertex, is_empty_graph, all_vertex_degree
from .xyz_common_code import get_x_vector, get_y_vector, get_z_vector


# TODO: Benchmark
# np.argwhere(graph == np.amax(graph))
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


def xyz_algo(graph: np.ndarray, *args):
    sparse = build_sparse(graph)
    cover_group = []

    while True:
        selected_vertex = xyz_select_vertex(sparse)
        if selected_vertex is None:
            break
        zero_vertex(sparse, selected_vertex)
        cover_group.append(selected_vertex)
    return cover_group
