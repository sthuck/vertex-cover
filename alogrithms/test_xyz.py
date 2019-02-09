import igraph
from numpy.testing import assert_equal, assert_array_almost_equal
from numpy import matrix
import graph_utils

from alogrithms import xyz

graph = xyz.build_sparse(graph_utils.graph_to_numpy(igraph.Graph(n=5, edges=[(0, 2), (1, 2), (3, 4), (4, 1)])))
expected_degrees = [1, 2, 2, 1, 2]


def test_degrees():
    assert_equal(xyz.all_vertex_degree(graph), matrix(expected_degrees))


def test_x_vector():
    expected_x = [1 / 2, 2 / 3, 2 / 3, 1 / 2, 2 / 3]
    assert_equal(xyz.get_x_vector(xyz.all_vertex_degree(graph)), matrix(expected_x))


def test_y_vector():
    x = [1 / 2, 2 / 3, 2 / 3, 1 / 2, 2 / 3]
    expected_y = [
        x[0] + x[2],
        x[1] + x[2] + x[4],
        x[2] + x[1] + x[0],
        x[3] + x[4],
        x[4] + x[1] + x[3]
    ]

    degree_vector = xyz.all_vertex_degree(graph)
    x_vector = xyz.get_x_vector(degree_vector)
    assert_array_almost_equal(xyz.get_y_vector(graph, x_vector), matrix(expected_y))


def test_z_vector():
    # edges=[(0, 2), (1, 2), (3, 4), (4, 1)])
    # degrees = [1, 2, 2, 1, 2];
    expected_z = [
        # v0 has 1 neighbour - v2. after removing v0, v2 has degree 1
        (1 / 2) + 1,
        # v1 has 2 neighbours - v2, v4. after removing v1, v2 has degree 1, v4 has degree 1
        (1 / 2) + (1 / 2) + 1,
        # v2 has 2 neighbours - v0, v1. after removing v2, v0 has degree 0, v1 has degree 1
        (0 / 1) + (1 / 2) + 1,
        # v3 has 1 neighbours - v4. after removing v3, v4 has degree 1
        (1 / 2) + 1,
        # v4 has 2 neighbours - v3, v1. after removing v4, v3 has degree 0, v1 has degree 1
        (0 / 1) + (1 / 2) + 1,
    ]

    degree_vector = xyz.all_vertex_degree(graph)
    assert_array_almost_equal(xyz.get_z_vector(graph, degree_vector), matrix(expected_z))


def test_is_empty():
    assert_equal(xyz.is_empty_graph(xyz.build_sparse([0, 0, 0, 0, 0])), True)
    assert_equal(xyz.is_empty_graph(xyz.build_sparse([0, 0, 1, 0, 0])), False)
