from numpy.testing import assert_equal
from unittest import TestCase
from bwc.bwc_algo import bwc_algo
from igraph import Graph

class TestBwcAlgo(TestCase):

    def test_algorithm(self):
        graph = Graph(n=4, edges=[(0, 1), (1, 2), (2, 0)])
        for v in graph.vs:
            v['__index'] = v.index
        graph, C = bwc_algo(graph, 1)
        self.assertEqual(len(graph.vs) - len(C), 3)
        self.assertEqual([v['__index'] for v in graph.vs if v['__index'] not in C], [0,1,2])

    def test_algorithm_rail(self):
        edges = [(i, i+1) for i in range(0, 4)]
        graph = Graph(n=5, edges=edges)
        for v in graph.vs:
            v['__index'] = v.index
        graph, C = bwc_algo(graph, 1)
        print([v['__index'] for v in graph.vs if v['__index'] not in C])
        self.assertEqual(len(graph.vs) - len(C), 3)

    def test_algorithm_rail2(self):
        edges = [(i, i + 1) for i in range(0, 4)]
        graph = Graph(n=5, edges=edges)
        for v in graph.vs:
            v['__index'] = v.index
        graph, C = bwc_algo(graph, 2)
        print([v['__index'] for v in graph.vs if v['__index'] not in C])
        self.assertEqual(2, len(graph.vs) - len(C))

