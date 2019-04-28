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
def select_vertex(graph: np.ndarray):
    vertex_degree_vector = all_vertex_degree(graph)

    it = np.nditer(vertex_degree_vector, flags=['f_index'])

    while it[0] == 0:
        it.iternext()

    return it.index


def is_empty_graph(graph: np.ndarray):
    return not graph.any()


def shaked_algo_impl(graph: np.ndarray, *args):
    cover_group = []
    while not is_empty_graph(graph):
        selected_vertex = select_vertex(graph)
        zero_vertex(graph, selected_vertex)
        cover_group.append(selected_vertex)
    return cover_group
