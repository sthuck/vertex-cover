from algorithms import shaked_algo_impl
from algorithms import shaked_algo_impl_v2
from graph_utils import graph_to_numpy
from igraph import Graph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# for each c in cs, generate 100 graphs
# on each graph run 100 iteration, run naive algo

iterations = 10000
n = 1000
cs = np.arange(0.25, 10.1, 0.25)  # c = [0.25..10]


def theorem5():
    results = {}

    for c in cs:
        c_results = []
        print(f'c {c}')
        for i in range(iterations):
            if i % 10 == 0:
                print(f'graph iteration {i}')

            graph_results = []
            graph: Graph = Graph.Erdos_Renyi(n, c / n)
            orig = graph_to_numpy(graph)

            for j in range(iterations):
                np_graph = orig.copy()
                cover_group = shaked_algo_impl_v2.shaked_algo_impl_v2(np_graph, randomize=True)
                cover_group_size = len(cover_group)
                graph_results.append(cover_group_size)
            c_results.append(np.array(graph_results))
        results[c] = np.array(c_results)
    return results


def theorem4():
    results = {}

    for c in cs:
        c_results = []
        print(f'c {c}')
        for i in range(iterations):
            if i % 10 == 0:
                print(f'iteration {i}')

            graph: Graph = Graph.Erdos_Renyi(n, c / n)
            np_graph = graph_to_numpy(graph)

            cover_group = shaked_algo_impl_v2.shaked_algo_impl_v2(np_graph, randomize=True)
            cover_group_size = len(cover_group)
            c_results.append(cover_group_size)
        results[c] = c_results
    return results


if __name__ == '__main__':
    # results = theorem5()
    # data = np.array(list(results.values()))
    # np.save('./theorem5.npy', data )
    #
    # data = data.var(axis=2)
    # theorem5_results = pd.DataFrame(data).T
    # theorem5_results.columns = list(results.keys())
    # theorem5_results = theorem5_results.mean()
    # theorem5_results.name = 't5'
    # print(theorem5_results)


    results = theorem4()
    df = pd.DataFrame(results)
    theorem4_results = df.var()
    np.save('./theorem4.npy', df.to_numpy())

    theorem4_results.name = 't4'
    print(theorem4_results)

    # theorem5_results.plot(legend=True)
    theorem4_results.plot(legend=True)

    theorem4_results.to_csv('./theorem4_results.csv')
    # theorem5_results.to_csv('./theorem5_results.csv')


    # df = pd.DataFrame(results)
    # var = df.var()
    # print(var)
    # var.plot()



