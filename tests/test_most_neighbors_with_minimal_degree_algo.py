from unittest import TestCase
from algorithms import most_neighbors_with_minimal_degree
from igraph import Graph
from numpy.testing import assert_equal, assert_almost_equal
import graph_utils


class Test_Most_neighbors_with_minimal_degree_algo(TestCase):

    def test_find_maximum(self):
        item_list = [(i, v) for (i, v) in enumerate([1, 2, 10])]
        maximum = most_neighbors_with_minimal_degree.find_maximum(item_list)
        assert maximum == [2]

        item_list = [(i, v) for (i, v) in enumerate([1, 2, 10, 5, 10])]
        maximum = most_neighbors_with_minimal_degree.find_maximum(item_list)
        assert maximum == [2, 4]

        item_list = [(i, v) for (i, v) in enumerate([1, 2, 10, 5, 10, 10])]
        maximum = most_neighbors_with_minimal_degree.find_maximum(item_list)
        assert maximum == [2, 4, 5]

    def test_algorithm(self):
        graph = Graph.Erdos_Renyi(10, 0.3)
        cover = most_neighbors_with_minimal_degree.most_neighbors_with_minimal_degree_algo(None, graph)
        assert_equal(graph_utils.check_if_legal_vertex_cover(graph_utils.graph_to_numpy(graph), cover), True)

    def test_most_neighbors_with_minimal_degree_algo(self):
        graph = Graph(n=7, edges=[(0, 1), (0, 5), (1, 5), (1, 2), (2, 5), (2, 4), (4, 3), (4, 5), (3, 6)])
        cover_group = most_neighbors_with_minimal_degree.most_neighbors_with_minimal_degree_algo(None, graph)
        assert_equal(cover_group, [3, 5, 1, 2])
