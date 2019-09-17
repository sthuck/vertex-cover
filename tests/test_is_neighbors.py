from unittest import TestCase
from igraph import Graph
from algorithms.reductions.disjoint_neighbors import is_neighbors


class TestIs_neighbors(TestCase):
    def test_is_neighbors(self):
        graph = Graph(n=5, edges=[(1, 2), (3, 4), (4, 1)])
        self.assertTrue(is_neighbors((graph.vs[1], graph.vs[2])))
        self.assertTrue(is_neighbors((graph.vs[1], graph.vs[4])))
        self.assertFalse(is_neighbors((graph.vs[1], graph.vs[3])))
        self.assertFalse(is_neighbors((graph.vs[2], graph.vs[3])))

