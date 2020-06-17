import numpy as np
import scipy as sc


def all_vertex_degree(graph: np.ndarray):
    return graph.sum(axis=0)


def vertex_degree(graph: np.ndarray, vertex: int):
    return graph.sum(axis=0)[vertex]


def zero_vertex(graph: np.ndarray, vertex: int):
    graph[vertex] = 0
    graph[:, vertex] = 0


# TODO: Benchmark
# np.argwhere(graph == np.amax(graph))
def select_vertex(graph: np.ndarray, randomize):
    vertex_degree_vector: np.ndarray = all_vertex_degree(graph)
    nonzero = vertex_degree_vector.nonzero()
    num_non_zero = nonzero[0].shape[0]
    selected_vertex = np.random.randint(num_non_zero) if randomize else 0
    return nonzero[0][selected_vertex]


def is_empty_graph(graph: np.ndarray):
    return not graph.any()


def shaked_algo_impl(graph: np.ndarray, *args, **kwargs):
    randomize = kwargs.get('randomize') or False
    cover_group = []
    while not is_empty_graph(graph):
        selected_vertex = select_vertex(graph, randomize)
        zero_vertex(graph, selected_vertex)
        cover_group.append(selected_vertex)
    return cover_group
