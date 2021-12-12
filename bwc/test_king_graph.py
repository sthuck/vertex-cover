from unittest import TestCase
from bwc.king_graph import KingGraph


class TestKingGraph(TestCase):
    def test_get_neighbors_king(self):
        helper = KingGraph(3, 3)
        neighbors = helper._get_neighbors(0, 0)
        self.assertCountEqual(neighbors, [(0, 1), (1, 1), (1, 0)])
        neighbors = helper._get_neighbors(1, 1)
        self.assertCountEqual(neighbors,
                              [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])

