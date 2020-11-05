import numpy as np
import scipy as sc
from igraph import Graph, Vertex

def all_vertex_degree(graph: np.ndarray):
    return graph.sum(axis=0)


def to_boxes(degree_vector: np.ndarray):
    values = np.unique(degree_vector)
    boxes = [(v, (np.argwhere(degree_vector == v)[:, 0])) for v in values]
    boxes.sort(key=lambda tup: -tup[0])
    return boxes


def zero_vertex(graph: np.ndarray, vertex: int, degree_vector: np.ndarray):
    neighbors = graph[vertex].nonzero()
    graph[vertex] = 0
    graph[:, vertex] = 0
    degree_vector[neighbors] = degree_vector[neighbors] - 1
    degree_vector[vertex] = 0


def degree_minus(graph: np.ndarray, igraph_graph: Graph, *args, **kwargs):
    # randomize = kwargs.get('randomize') or False
    if igraph_graph:
        print(f'degree_minus expected: {degree_minus_expected}')

    cover_group = []
    vertex_degree_vector = all_vertex_degree(graph)
    boxes = to_boxes(vertex_degree_vector)

    for (original_rank, box) in boxes:
        for selected_vertex in box:
            if vertex_degree_vector[selected_vertex] > 0:
                zero_vertex(graph, selected_vertex, vertex_degree_vector)
                cover_group.append(selected_vertex)

    return cover_group


def isInA(v: Vertex):
    degree = v.degree()
    neighbors_with_lower_degree = [n for n in v.neighbors() if n.degree() < degree]
    return len(neighbors_with_lower_degree) > 0


def b_v(v: Vertex):
    degree = v.degree()
    neighbors_with_lower_degree = [n for n in v.neighbors() if n.degree() == degree]
    return len(neighbors_with_lower_degree)


def b_v_divide_b_v_1(v: Vertex):
    bv = b_v(v)
    return bv/(bv + 1)


def degree_minus_expected(graph: Graph):
    A = {v for v in graph.vs if isInA(v)}
    not_in_a = {v for v in graph.vs if v not in A}
    bv_sigma = sum([b_v_divide_b_v_1(v) for v in not_in_a])
    return bv_sigma + len(A)
