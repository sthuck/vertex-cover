from algorithms import neighbors
from igraph import Graph
from numpy.testing import assert_equal
import graph_utils


def test_find_vertex_with_neighbours():
    graph1 = Graph(n=5, edges=[(4, 1), (2, 3)])
    graph2 = Graph(n=5, edges=[(2, 0), (1, 2), (3, 4), (4, 1)])
    assert_equal(neighbors.find_vertex_with_neighbours(graph1).index, 1)
    assert_equal(neighbors.find_vertex_with_neighbours(graph2).index, 0)


def test_select_vertices():
    graph = Graph(n=5, edges=[(2, 0), (1, 2), (0, 4), (4, 1)])
    neighbors.set_name(graph)
    assert_equal(neighbors.select_vertices(graph), [2, 4])


def test_zero_vertices():
    graph = Graph(n=5, edges=[(2, 0), (1, 2), (0, 4), (4, 1)])
    neighbors.set_name(graph)
    neighbors.zero_vertices(graph, [2, 4])
    assert_equal([v['name'] for v in graph.vs], [0, 1, 3])


def test_algorithm():
    graph = Graph.Erdos_Renyi(100, 0.05)
    cover = neighbors.neighbors_algo(None, graph)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph_utils.graph_to_numpy(graph), cover), True)
