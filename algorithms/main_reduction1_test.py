from algorithms.novac1 import novac1_algo
from algorithms.xyz import xyz_v3_algo_with_reductions, xyz_v3_algo_without_reductions
from algorithms.degree import degree
from graph_utils import random_graph, graph_to_numpy, set_name
from algorithms.reductions import reduce_graph
import pandas as pd
import numpy as np
from typing import List
from igraph import Graph

def stand_alone_run():
    n = 1000
    start = 2.65
    step = 0.01
    stop = 2.65
    iterations = 1
    lambda_array = np.arange(start, stop + step, step)

    for c in lambda_array:
        p = c / n

        for i in range(iterations):
            print(f'c: {c}, iteration {i}:')
            graph = random_graph(n, p)
            set_name(graph)

            add_to_cover, removed_count = reduce_graph(graph, do_reduce_1=True, do_reduce_2=False, do_reduce_3=False)
            print(f'1. how many added to cover: {len(add_to_cover) + removed_count}')
            # 1. how many added to cover
            # 2. how many left in graph
            print(f'2. how many left in graph: {len(graph.vs)}')
            # 3. for each cc, is it a circle (every vertex degree is 2, vertex_number = Edge number)
            for component in graph.components():
                is_component_circle = is_circle(graph, component)
                print(f'cc: is circle {is_component_circle}')
                if not is_component_circle:
                    print(f'\t cc size: {len(component)}')


def is_circle(graph: Graph, vertex_list: List[int]):
    all_degree_2 = all(graph.vs[v].degree() == 2 for v in vertex_list)
    subgraph = graph.subgraph(vertex_list)
    edge_number_equal_n = len(subgraph.es) == len(vertex_list)
    return all_degree_2 and edge_number_equal_n


#    return
if __name__ == "__main__":
    stand_alone_run()