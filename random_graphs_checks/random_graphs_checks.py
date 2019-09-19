from igraph import Graph
from igraph import Vertex
from typing import Tuple, List
from graph_utils import set_name
from algorithms.reductions import reduce_graph, remove_parents_of_leaves, print_graph_info, print_theortical_number_of_leaves


def run_reduce_1_by_iteration(graph=None):
    n = 1000
    c = 3
    graph: Graph = graph or Graph.Erdos_Renyi(n, c / n)
    set_name(graph)

    print_theortical_number_of_leaves(n, c)
    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='initial graph')
    added_to_cover = remove_parents_of_leaves(graph, log=True, one_time=False)
    print(f'how many added to cover: {len(added_to_cover)}')


def run_reduce_graph_compare(graph=None):
    graph: Graph = graph or Graph.Erdos_Renyi(10000, 2.8 / 10000)
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
    graph: Graph = graph or Graph.Erdos_Renyi(100, 3 / 100)
    set_name(graph)

    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='start')
    added_to_cover, counter_of_removed = reduce_graph(graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=True)
    print(f'size of cover: {len(added_to_cover) + counter_of_removed}')
    print_graph_info(graph, leaves=True, zero_degree=True, connected_components=True, label='end')


if __name__ == '__main__':
    run_reduce_1_by_iteration()
    # run_reduce_graph_compare()
    # run_reduce_graph_all()
