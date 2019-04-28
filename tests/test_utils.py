from igraph import Graph
from numpy.testing import assert_equal
import graph_utils


def test_check_if_legal_vertex_cover():
    graph = graph_utils.graph_to_numpy(Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)]))
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [1, 3]), True)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [1, 4]), True)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [3, 4]), False)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [1]), False)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [0]), False)


def test_count_parents_of_leaves():
    graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)])
    assert_equal(graph_utils.count_parents_of_leaves(graph), 2)

    graph = Graph(n=5, edges=[(1, 2), (3, 1), (4, 1)])
    assert_equal(graph_utils.count_parents_of_leaves(graph), 1)

    # Two vertices with rank 1
    graph = Graph(n=5, edges=[(1, 2), (3, 1), (4, 1), (0, 5)])
    assert_equal(graph_utils.count_parents_of_leaves(graph), 2)

    # Multiple parents
    graph = Graph(n=5, edges=[(1, 2), (3, 1), (4, 1), (0, 5)])
    assert_equal(graph_utils.count_parents_of_leaves(graph), 2)

    graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1), (5, 4), (5, 0)])
    assert_equal(graph_utils.count_parents_of_leaves(graph), 3)
