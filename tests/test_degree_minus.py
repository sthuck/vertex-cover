from numpy.testing import assert_equal
import graph_utils
from unittest import TestCase
from igraph import Graph
from algorithms.degree_minus import degree_minus, isInA


class TestDegreeMinus(TestCase):

    def test_algorithm(self):
        graph = graph_utils.graph_to_numpy(Graph(n=3, edges=[(0, 1), (0, 2), (1, 2)]))
        cover_group = degree_minus(graph)
        assert_equal(len(cover_group), 2)

    # def test_algorithm2(self):
    #     graph = graph_utils.graph_to_numpy(Graph(n=3, edges=[(0, 1), (0, 2), (1, 2)]))
    #     cover_group = degree_minus(graph)
    #     assert_equal(cover_group, [0, 1])

    def test_random_graphs(self):
        for i in range(10):
            graph = graph_utils.random_graph(100, 0.1)
            g = graph_utils.graph_to_numpy(graph)
            cover = degree_minus(g)
            assert (graph_utils.check_if_legal_vertex_cover(g, cover))

    def test_is_in_a(self):
        graph = Graph(n=5, edges=[(0, 1), (1, 2), (2, 3), (3,4), (4,0)])
        A = [v for v in graph.vs if isInA(v)]
        assert(len(A) == 0)