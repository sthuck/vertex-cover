from unittest import TestCase
from igraph import Graph
from prop1 import graph_data

class TestProp1(TestCase):
    def testdv_divide_dv_1_squared(self):
        graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)]) #0 2 1 1 2
        expected = 2/9 + 1/4 + 1/4 + 2/9
        self.assertEqual(graph_data.dv_divide_dv_1_squared(graph), expected)

    def test_find_common_neighbors(self):
        graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)]) #0 2 1 1 2
        self.assertEqual(graph_data.find_common_neighbors(graph, 1, 2), 0)
        self.assertEqual(graph_data.find_common_neighbors(graph, 1, 3), 1)
        self.assertEqual(graph_data.find_common_neighbors(graph, 2, 4), 1)
        self.assertEqual(graph_data.find_common_neighbors(graph, 0, 4), 0)

    def test_compute_third_thing_shaked_find_a_better_names(self):
        graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)]) #0 2 1 1 2
        self.assertGreater(graph_data.compute_third_thing_shaked_find_a_better_name(graph), 0)


