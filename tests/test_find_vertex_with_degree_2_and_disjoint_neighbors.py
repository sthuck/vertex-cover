from random_graphs_checks import find_vertex_with_degree_2_and_disjoint_neighbors
from unittest import TestCase
from igraph import Graph


class TestFind_vertex_with_degree_2_and_disjoint_neighbors(TestCase):
    def test_find_vertex_with_degree_2_and_disjoint_neighbors(self):
        graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)])
        self.assertEqual(find_vertex_with_degree_2_and_disjoint_neighbors(graph).index, 1)
        graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1), (4,2)])
        self.assertEqual(find_vertex_with_degree_2_and_disjoint_neighbors(graph), None)



