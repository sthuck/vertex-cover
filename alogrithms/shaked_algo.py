import numpy as np


def all_vertex_degree(graph: np.ndarray):
    return graph.sum(axis=0)


def shaked_algo(graph: np.ndarray):
    degree_vector = all_vertex_degree(graph)
    degree_vector_plus_one = degree_vector + 1
    division_result = (degree_vector / degree_vector_plus_one)
    return division_result.sum()

