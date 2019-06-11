from algorithms import new_algo
from igraph import Graph
from numpy.testing import assert_equal
import graph_utils


def test_algorithm():
    graph = Graph.Erdos_Renyi(100, 0.05)
    cover = new_algo.new_algo(None, graph)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph_utils.graph_to_numpy(graph), cover), True)
