import scipy.sparse as sp
import numpy
from typing import Union
from igraph import Graph


def zero_vertex(graph: sp.spmatrix, vertex: int):
    graph[vertex] = 0
    graph[:, vertex] = 0


def all_vertex_degree(graph: sp.spmatrix) -> numpy.ndarray:
    return graph.sum(axis=0).getA()[0]


def build_sparse(graph: numpy.ndarray):
    return sp.lil_matrix(graph)


def is_empty_graph(graph: sp.spmatrix):
    return graph.count_nonzero() == 0
