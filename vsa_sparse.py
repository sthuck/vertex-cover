import numpy as np
import scipy.sparse as sp


def all_vertex_degree(graph: np.ndarray):
    return graph.sum(axis=0)


def vertex_degree(graph: sp.csr_matrix, vertex: int):
    return graph.sum(axis=0)[vertex]


def vertex_support_all(graph: sp.csr_matrix, degree_vector=None):
    degrees = degree_vector if degree_vector is not None else all_vertex_degree(graph)
    # return (graph * degrees).sum(axis=1)
    return (degrees * graph).A[0]


def zero_vertex(graph: np.ndarray, vertex: int):
    graph[vertex] = 0
    graph[:, vertex] = 0


def build_sparse(graph):
    return sp.csc_matrix(graph)


# TODO: Benchmark
# np.argwhere(graph == np.amax(graph))
def vsa_select_vertex(graph: np.ndarray):
    sparse = build_sparse(graph)

    vertex_degree_vector = all_vertex_degree(sparse)
    vertex_support_vector = vertex_support_all(sparse, vertex_degree_vector)

    it = np.nditer(vertex_support_vector, flags=['f_index'])

    max_support = -1
    max_index = []
    while not it.finished:
        if it[0] > max_support:
            max_support = it[0]
            max_index = [it.index]
        elif it[0] == max_support:
            max_index.append(it.index)
        it.iternext()
    if len(max_index) == 1:
        return max_index[0]
    else:
        largest_degree_index = max(max_index, key=lambda index: vertex_degree_vector[0, index])
        return largest_degree_index


def is_empty_graph(graph: np.ndarray):
    return not graph.any()


def vsa(graph: np.ndarray):
    support_group = []
    i = 0
    while not is_empty_graph(graph):
        i = i + 1
        if i % 100 == 0:
            print(i)
        selected_vertex = vsa_select_vertex(graph)
        zero_vertex(graph, selected_vertex)
        support_group.append(selected_vertex)
    return support_group
