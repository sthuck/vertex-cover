from numpy.testing import assert_equal
import graph_utils
from unittest import TestCase
from algorithms.reductions.disjoint_neighbors import is_neighbors

from algorithms.shaked_algo_impl_v2 import all_vertex_degree, zero_vertex, shaked_algo_impl_v2
from algorithms.shaked_algo_impl import shaked_algo_impl


class TestIs_shaked_algo_impl_v2(TestCase):
    def test_zero_vertex(self):
        graph = graph_utils.random_graph(10, 0.3)
        npgraph = graph_utils.graph_to_numpy(graph)
        degree_vector = all_vertex_degree(npgraph)
        zero_vertex(npgraph, 4, degree_vector)
        degree_vector_check = all_vertex_degree(npgraph)
        assert_equal(degree_vector, degree_vector_check)

    def test_algorithm(self):
        for i in range(10):
            graph = graph_utils.random_graph(100, 0.1)
            g1 = graph_utils.graph_to_numpy(graph)
            g2 = graph_utils.graph_to_numpy(graph)
            cover_group1 = shaked_algo_impl_v2(g1)
            cover_group2 = shaked_algo_impl(g2)
            assert_equal(cover_group1, cover_group2)


