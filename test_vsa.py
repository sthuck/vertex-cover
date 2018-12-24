import pytest
import igraph
from numpy.testing import assert_equal
from numpy import array as nd
import graph_utils
import random

import vsa


def test_degree():
    graph = graph_utils.graph_to_numpy(igraph.Graph.Full(5))
    assert_equal(vsa.all_vertex_degree(graph), [4, 4, 4, 4, 4])

    graph = graph_utils.graph_to_numpy(igraph.Graph.Ring(5))
    assert_equal(vsa.all_vertex_degree(graph), [2, 2, 2, 2, 2])

    graph = graph_utils.graph_to_numpy(igraph.Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)]))
    assert_equal(vsa.all_vertex_degree(graph), [0, 2, 1, 1, 2])


def test_vertex_support_all():
    graph = graph_utils.graph_to_numpy(igraph.Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)]))
    assert_equal(vsa.vertex_support_all(graph), [0, 3, 2, 2, 3])


def test_is_empty():
    assert_equal(vsa.is_empty_graph(nd([0, 0, 0, 0, 0])), True)
    assert_equal(vsa.is_empty_graph(nd([0, 0, 1, 0, 0])), False)
