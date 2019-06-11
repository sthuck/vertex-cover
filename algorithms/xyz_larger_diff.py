import numpy as np
import scipy.sparse as sp
import scipy


def all_vertex_degree(graph: sp.csr_matrix):
    return graph.sum(axis=0)


def zero_vertex(graph: sp.lil_matrix, vertex: int):
    graph[vertex] = 0
    graph[:, vertex] = 0


def build_sparse(graph):
    return sp.lil_matrix(graph)


# TODO: Benchmark
# np.argwhere(graph == np.amax(graph))
def xyz_select_vertex(graph: sp.lil_matrix):
    sparse = graph.tocsr()

    if is_empty_graph(sparse):
        return None

    vertex_degree_vector = all_vertex_degree(sparse).A1

    x_vector = get_x_vector(vertex_degree_vector)
    y_vector = get_y_vector(sparse, x_vector)
    z_vector = get_z_vector(sparse, vertex_degree_vector)

    diff_vector = z_vector - y_vector
    index_diff_tuple_vector = [(index, diff) for (index, diff) in enumerate(diff_vector)]
    index_diff_tuple_vector.sort(key=lambda tup: -tup[1])

    largest_diff_but_has_neighbours = None

    i = 0
    while largest_diff_but_has_neighbours is None:
        candidate = index_diff_tuple_vector[i][0]
        if vertex_degree_vector[candidate] != 0:
            largest_diff_but_has_neighbours = candidate
        else:
            i = i + 1

    return largest_diff_but_has_neighbours


def get_z_vector(sparse, vertex_degree_vector):
    # take rank and decrease by 1, unless rank is already 0
    degree_minus_1_vector: scipy.matrix = np.select([vertex_degree_vector > 0, vertex_degree_vector == 0],
                                                    [vertex_degree_vector - 1,
                                                     vertex_degree_vector])
    temp_x_vector = get_x_vector(degree_minus_1_vector)
    z_vector = (temp_x_vector * sparse) + 1
    return z_vector


def get_y_vector(sparse, x_vector):
    return (x_vector * sparse) + x_vector


def get_x_vector(vertex_degree_vector):
    return vertex_degree_vector / (vertex_degree_vector + 1)


def is_empty_graph(graph: sp.lil_matrix):
    return graph.count_nonzero() == 0


def xyz_larger_diff_algo(graph: np.ndarray, *args):
    sparse = build_sparse(graph)
    cover_group = []

    while True:
        selected_vertex = xyz_select_vertex(sparse)
        if selected_vertex is None:
            break
        zero_vertex(sparse, selected_vertex)
        cover_group.append(selected_vertex)
    return cover_group
