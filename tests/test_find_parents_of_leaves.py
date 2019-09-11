import igraph
from numpy.testing import assert_equal, assert_array_almost_equal
from random_graphs_checks import p0002_graph, p0003_graph


def test_p0003_graph():
    for i in range(1000):
        print(f'iteration {i}')
        # orig_graph = igraph.Graph.Erdos_Renyi(20, 2 / 10)
        orig_graph = igraph.Graph.Read_GraphMLz('./demo.graph', directed=False)
        graph = orig_graph.copy()
        results = p0003_graph(graph)
        if len(results['component_length_vector']) > 0 and results['component_length_vector'][0] == 2:
            print('oops')
        else:
            print(results)
