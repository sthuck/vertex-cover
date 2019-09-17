from algorithms import xyz_neighbors_combined
from igraph import Graph
from numpy.testing import assert_equal, assert_almost_equal
import graph_utils


def test_algorithm():
    graph = Graph.Erdos_Renyi(100, 0.05)
    cover = xyz_neighbors_combined.xyz_neighbors_combined_algo(None, graph)
    assert_equal(graph_utils.check_if_legal_vertex_cover(graph_utils.graph_to_numpy(graph), cover), True)


def test_compute_k():
    graph = Graph(n=7, edges=[(0, 1), (0, 5), (1, 5), (1, 2), (2, 5), (2, 4), (3, 6), (3, 4), (4, 5)])
    assert_almost_equal(xyz_neighbors_combined.compute_k(graph, graph.vs[0]), 5.08, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_k(graph, graph.vs[1]), 4.83, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_k(graph, graph.vs[2]), 4.91, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_k(graph, graph.vs[3]), 4.63, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_k(graph, graph.vs[4]), 4.83, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_k(graph, graph.vs[5]), 4.66, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_k(graph, graph.vs[6]), 5.21, decimal=2)


def test_compute_t():
    graph = Graph(n=7, edges=[(0, 1), (0, 5), (1, 5), (1, 2), (2, 5), (2, 4), (3, 6), (3, 4), (4, 5)])
    assert_almost_equal(xyz_neighbors_combined.compute_t(graph, graph.vs[0]), 4.33, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_t(graph, graph.vs[1]), 4.66, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_t(graph, graph.vs[2]), 4, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_t(graph, graph.vs[3]), 4.83, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_t(graph, graph.vs[4]), 4, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_t(graph, graph.vs[5]), 5, decimal=2)
    assert_almost_equal(xyz_neighbors_combined.compute_t(graph, graph.vs[6]), 4.63, decimal=2)


def test_select_vertices():
    graph = Graph(n=7, edges=[(0, 1), (0, 5), (1, 5), (1, 2), (2, 5), (2, 4), (3, 6), (3, 4), (4, 5)])
    xyz_neighbors_combined.set_name(graph)
    assert (xyz_neighbors_combined.select_vertices(graph) == (['v1', 'v4', 'v5'], ['v2']))
