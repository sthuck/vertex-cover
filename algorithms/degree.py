import numpy as np
import random

def all_vertex_degree(graph: np.ndarray):
    return graph.sum(axis=0)


def is_empty_graph(graph: np.ndarray):
    return not graph.any()


def zero_vertex(graph: np.ndarray, vertex: int):
    graph[vertex] = 0
    graph[:, vertex] = 0


def select_vertex(graph: np.ndarray):
    degree_vector: np.ndarray = all_vertex_degree(graph)
    random_vector = np.array([random.random() for i in range(len(degree_vector))])
    fake_degree_vector = random_vector + degree_vector
    return np.argmax(fake_degree_vector)


def degree(graph: np.ndarray, *args):
    cover_group = []
    while not is_empty_graph(graph):
        selected_vertex = select_vertex(graph)
        zero_vertex(graph, selected_vertex)
        cover_group.append(selected_vertex)
    return cover_group
