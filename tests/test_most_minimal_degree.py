from algorithms import most_minimal_degree
from igraph import Graph
from numpy.testing import assert_equal, assert_almost_equal
import graph_utils


def test_find_maximum():
    item_list = [1, 2, 10]
    maximum = most_minimal_degree.find_maximum(item_list)
    assert maximum == [2]

    item_list = [1, 2, 10, 5, 10]
    maximum = most_minimal_degree.find_maximum(item_list)
    assert maximum == [2, 4]

    item_list = [1, 2, 10, 5, 10, 10]
    maximum = most_minimal_degree.find_maximum(item_list)
    assert maximum == [2, 4, 5]

    item_list = [1, 2, 10, 5, 10, 10]
    maximum = most_minimal_degree.find_maximum(item_list, [0, 1, 3])
    assert maximum == [3]

    item_list = [1, 2, 10, 5, 10, 9]
    maximum = most_minimal_degree.find_maximum(item_list, [0, 1, 5])
    assert maximum == [5]


def test_algorithm():
    graph = Graph.Erdos_Renyi(10, 0.3)
    cover = most_minimal_degree.most_minimal_degree_algo(None, graph)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph_utils.graph_to_numpy(graph), cover), True)
