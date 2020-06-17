import numpy as np
import scipy as sc


def all_vertex_degree(graph: np.ndarray):
    return graph.sum(axis=0)


def zero_vertex(graph: np.ndarray, vertex: int, degree_vector: np.ndarray):
    neighbors = graph[vertex].nonzero()
    graph[vertex] = 0
    graph[:, vertex] = 0
    degree_vector[neighbors] = degree_vector[neighbors] - 1
    degree_vector[vertex] = 0


# TODO: Benchmark
# np.argwhere(graph == np.amax(graph))
def select_vertex(graph: np.ndarray, randomize, vertex_degree_vector: np.ndarray):
    # vertex_degree_vector: np.ndarray = all_vertex_degree(graph)
    nonzero = vertex_degree_vector.nonzero()
    num_non_zero = nonzero[0].shape[0]
    selected_vertex = np.random.randint(num_non_zero) if randomize else 0
    return nonzero[0][selected_vertex]


def is_empty_graph(graph: np.ndarray):
    return not graph.any()


def shaked_algo_impl_v2(graph: np.ndarray, *args, **kwargs):
    randomize = kwargs.get('randomize') or False
    cover_group = []
    vertex_degree_vector = all_vertex_degree(graph)
    while not is_empty_graph(graph):
        selected_vertex = select_vertex(graph, randomize, vertex_degree_vector)
        zero_vertex(graph, selected_vertex, vertex_degree_vector)
        cover_group.append(selected_vertex)
    return cover_group
