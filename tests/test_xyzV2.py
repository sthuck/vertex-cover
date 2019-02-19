import igraph
from numpy.testing import assert_equal, assert_array_almost_equal
from graph_utils import *
import pytest

from alogrithms import xyzV2
from alogrithms import xyz


graph = xyzV2.build_sparse(graph_to_numpy(igraph.Graph(n=5, edges=[(0, 2), (1, 2), (3, 4), (4, 1)])))
expected_degrees = [1, 2, 2, 1, 2]


def test_degrees():
    assert_equal(xyzV2.all_vertex_degree(graph), expected_degrees)


def test_x_vector():
    expected_x = [1 / 2, 2 / 3, 2 / 3, 1 / 2, 2 / 3]
    assert_equal(xyzV2.get_x_vector(xyzV2.all_vertex_degree(graph)), expected_x)


def test_y_vector():
    x = [1 / 2, 2 / 3, 2 / 3, 1 / 2, 2 / 3]
    expected_y = [
        x[0] + x[2],
        x[1] + x[2] + x[4],
        x[2] + x[1] + x[0],
        x[3] + x[4],
        x[4] + x[1] + x[3]
    ]

    degree_vector = xyzV2.all_vertex_degree(graph)
    x_vector = xyzV2.get_x_vector(degree_vector)
    assert_array_almost_equal(xyzV2.get_y_vector(graph, x_vector), expected_y)


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

    degree_vector = xyzV2.all_vertex_degree(graph)
    assert_array_almost_equal(xyzV2.get_z_vector(graph, degree_vector), expected_z)


def test_is_empty():
    assert_equal(xyzV2.is_empty_graph(xyzV2.build_sparse([0, 0, 0, 0, 0])), True)
    assert_equal(xyzV2.is_empty_graph(xyzV2.build_sparse([0, 0, 1, 0, 0])), False)


# TEST UNIQE FOX XYZ V2

def test_find_leaves():
    assert_equal(xyzV2.get_all_leaves(graph), [0, 3])


def test_find_leaves_no_leaves():
    full_graph = xyzV2.build_sparse(graph_to_numpy(igraph.Graph.Full(5)))
    assert_equal(xyzV2.get_all_leaves(full_graph), [])


def test_get_leaf_parent():
    assert_equal(xyzV2.get_parent_of_leaf(graph, 3), 4)


@pytest.mark.focus
def test_xyz_and_v2_impl_equal():
    new_graph = graph_to_numpy(random_graph(100, 0.1))
    result1 = xyz.xyz_algo(new_graph.copy())
    result2 = xyzV2.xyz_v2_algo(new_graph.copy())
    result1.sort()
    result2.sort()
    assert_equal(result1, result2)

