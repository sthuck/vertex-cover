from algorithms import shaked_algo_impl
from algorithms import shaked_algo_impl_v2
from algorithms.degree import degree
from graph_utils import graph_to_numpy
from igraph import Graph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# for each c in cs, run 100 iterations
# on each iteration run naive algo

def main():
    iterations = 200
    n = 1000
    cs = np.arange(0.5, 0.75, 0.25) # c = [0.25..10]
    results = {}

    for c in cs:
        c_results = []
        print(f'c {c}')
        for i in range(iterations):
            if i % 10 == 0:
                print(f'iteration {i}')

            graph: Graph = Graph.Erdos_Renyi(n, c / n)
            np_graph = graph_to_numpy(graph)

            cover_group = degree(np_graph)
            #cover_group = shaked_algo_impl_v2.shaked_algo_impl_v2(np_graph, randomize=True)
            cover_group_size = len(cover_group)
            c_results.append(cover_group_size)
        results[c] = c_results
    return results


if __name__ == '__main__':
    results = main()
    df = pd.DataFrame(results)
    mean = df.mean()
    print(mean)
    #var.plot()


