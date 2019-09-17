from igraph import Graph
from igraph import Vertex
from typing import Tuple, List
from graph_utils import set_name
from algorithms.reductions import reduce_graph, remove_parents_of_leaves, print_graph_info


def run_reduce_1_once(graph=None):
    graph: Graph = graph or Graph.Erdos_Renyi(1000, 2 / 1000)
    set_name(graph)

    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='start')
    remove_parents_of_leaves(graph, one_time=True)
    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='end')


def run_reduce_graph_compare(graph=None):
    graph: Graph = graph or Graph.Erdos_Renyi(1000, 3 / 1000)
    copy1 = graph.copy()
    copy2 = graph.copy()
    set_name(copy1)
    set_name(copy2)

    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='initial graph')

    reduce_graph(copy1, do_reduce_1=True, do_reduce_2=False, do_reduce_3=False)
    print_graph_info(copy1, leaves=True, zero_degree=True, connected_components=True, label='copy1: after only reduce 1')

    reduce_graph(copy2, do_reduce_1=True, do_reduce_2=True, do_reduce_3=False)
    print_graph_info(copy2, leaves=True, zero_degree=True, connected_components=True, label='copy2: after reduce 1 + 2')


def run_reduce_graph_all(graph=None):
    graph: Graph = graph or Graph.Erdos_Renyi(1000, 2 / 1000)
    set_name(graph)

    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='start')
    reduce_graph(graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=True)
    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='end')


if __name__ == '__main__':
    # print(p0002_graph())
    run_reduce_graph_compare()
