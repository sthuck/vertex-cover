import numpy as np
import scipy as sc


def all_vertex_degree(graph: np.ndarray):
    return graph.sum(axis=0)


def vertex_degree(graph: np.ndarray, vertex: int):
    return graph.sum(axis=0)[vertex]


def vertex_support_all(graph: np.ndarray, degree_vector=None):
    degrees = degree_vector if degree_vector is not None else all_vertex_degree(graph)
    # return (graph * degrees).sum(axis=1)
    return graph.dot(degrees)


def zero_vertex(graph: np.ndarray, vertex: int):
    graph[vertex] = 0
    graph[:, vertex] = 0
    

# TODO: Benchmark
# np.argwhere(graph == np.amax(graph))
def vsa_select_vertex(graph: np.ndarray):
    vertex_degree_vector = all_vertex_degree(graph)
    vertex_support_vector = vertex_support_all(graph, vertex_degree_vector)

    it = np.nditer(vertex_degree_vector, flags=['f_index'])

    max_degree = -1
    max_index = []
    while not it.finished:
        if it[0] > max_degree:
            max_degree = it[0]
            max_index = [it.index]
        elif it[0] == max_degree:
            max_index.append(it.index)
        it.iternext()

    if len(max_index) == 1:
        return max_index[0]
    else:
        smallest_support_index = min(max_index, key=lambda index: vertex_support_vector[index])
        return smallest_support_index


def is_empty_graph(graph: np.ndarray):
    return not graph.any()


def vsa_by_min(graph: np.ndarray):
    cover_group = []
    while not is_empty_graph(graph):
        selected_vertex = vsa_select_vertex(graph)
        zero_vertex(graph, selected_vertex)
        cover_group.append(selected_vertex)
    return cover_group
