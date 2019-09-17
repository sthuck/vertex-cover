from unittest import TestCase
from igraph import Graph
from algorithms.reductions import remove_vertex_if_contained_neighbors
from graph_utils import set_name


class TestRemove_vertex_if_contained_neighbors(TestCase):
    def test_remove_vertex_if_contained_neighbors(self):
        graph = Graph(n=8, edges=[(1, 3), (3, 4), (4, 1), (1, 2), (3, 2), (2, 5), (5, 4)])
        set_name(graph)

        add_to_cover = remove_vertex_if_contained_neighbors(graph)
        self.assertEqual(add_to_cover, ['v1'])
