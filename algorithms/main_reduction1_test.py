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
    n = 1000000
    c = 2.65
    # step = 0.01
    # stop = 2.69
    iterations =20
    # lambda_array = np.arange(start, stop + step, step)

    p = c / n
    results = {}
    for i in range(iterations):
        results[i] = {}
        print(f'c: {c}, iteration {i}:')
        graph = random_graph(n, p)
        set_name(graph)

        add_to_cover, removed_count = reduce_graph(graph, do_reduce_1=True, do_reduce_2=False, do_reduce_3=False)
        print(f'1. how many added to cover: {len(add_to_cover) + removed_count}')
        results[i]['how many added to cover'] = len(add_to_cover) + removed_count
        # 1. how many added to cover
        # 2. how many left in graph
        print(f'2. how many left in graph: {len(graph.vs)}')
        results[i]['how many left in graph'] = len(graph.vs)

        # 3. for each cc, is it a circle (every vertex degree is 2, vertex_number = Edge number)
        connected_components_not_circle = len([component for component in graph.components() if not is_circle(graph, component)])
        print(f'3. how many connected components not circles: {connected_components_not_circle}')
        results[i]['how many connected components not circles'] = connected_components_not_circle

    df = pd.DataFrame(results)
    df.to_csv('../main_reduction1_test.csv')
    return df


def is_circle(graph: Graph, vertex_list: List[int]):
    is_isolated = len(vertex_list) == 1 and graph.vs[vertex_list[0]].degree() == 0
    all_degree_2 = all(graph.vs[v].degree() == 2 for v in vertex_list)

    return is_isolated or all_degree_2


#    return
if __name__ == "__main__":
    df = stand_alone_run()