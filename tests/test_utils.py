import igraph
from numpy.testing import assert_equal
import graph_utils


def test_check_if_legal_vertex_cover():
    graph = graph_utils.graph_to_numpy(igraph.Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)]))
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [1, 3]), True)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [1, 4]), True)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [3, 4]), False)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [1]), False)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph, [0]), False)
