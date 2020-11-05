from algorithms import shaked_algo_impl
from algorithms import shaked_algo_impl_v2
from graph_utils import graph_to_numpy
from igraph import Graph
import numpy as np
import matplotlib.pyplot as plt

# On each iteration random graph
# on each sub-iteration run naive algo, as it's randomized

def main():
    iterations = 1
    sub_iteration = 0
    n = 10000
    c = 0.01
    results = []

    for i in range(iterations):
        if i % 10 == 0:
            print(f'iteration {i}')

        graph: Graph = Graph.Erdos_Renyi(n, c / n)
        np_graph = graph_to_numpy(graph)

        single_graph_results = []
        for j in range(sub_iteration):
            if i%10 == 0 and j % 10 == 0:
                print(f'   sub-iteration {j}')
            copy = np_graph.copy()
            cover_group = shaked_algo_impl_v2.shaked_algo_impl_v2(copy, randomize=True)
            cover_group_size = len(cover_group)
            single_graph_results.append(cover_group_size)

        results.append(single_graph_results)

    print('=========')
    avg_per_graph = np.array(results).mean(axis=1)
    avg_of_avgs = avg_per_graph.mean()
    print(f'average: {avg_of_avgs}')
    expected = ((np.power(np.e, -c) + c - 1)/c)*n
    print(f'expected: {expected}')

    variance_per_graph = np.array(results).var(axis=1)
    avg_of_variance_per_graph = variance_per_graph.mean()
    print(f'variance: {avg_of_variance_per_graph}')


if __name__ == '__main__':
     main()

