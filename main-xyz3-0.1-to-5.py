from graph_utils import *
from algorithms.xyz import xyz_v2_algo, xyz_v3_algo, xyz_v3_algo_with_reductions, \
    xyz_v3_algo_only_with_leaf_parent_reduction, xyz_v3_algo_without_reductions
from algorithms.novac1 import novac1_algo
from algorithms.degree import degree
import time
import numpy as np
import pandas as pd
from igraph import Graph
import random


def random_tree(n):
    graph = Graph()
    graph_size = n + 2
    graph.add_vertices(n=graph_size)
    a = [random.randint(0, graph_size - 1) for i in range(n)]
    assert len(a) == n
    degree = [1 for _ in range(graph_size)]

    for i in a:
        degree[i] = degree[i] + 1
    for i in a:
        for j in range(graph_size):
            if degree[j] == 1:
                graph.add_edge(i, j)
                degree[i] = degree[i] - 1
                degree[j] = degree[j] - 1
                break
    u = None
    v = None
    for i in range(graph_size):
        if degree[i] == 1:
            if u is None:
                u = i
            else:
                v = i
                break
    graph.add_edge(u, v)
    degree[u] = degree[u] - 1
    degree[v] = degree[v] - 1

    return graph


# returns list 3 items
def run_graph(algorithms, n, c, iterations=20) -> int:
    print(f'running for n value: {n}')
    # print(f'running for c value: {c}')
    results = {algo.__name__: [] for algo in algorithms}
    for i in range(iterations):
        print(f'running iteration {i}')
        p = c / n

        # orig = random_graph(n, p)
        orig = random_tree(n)

        for algo in algorithms:
            graph = orig.copy()
            np_graph = graph_to_numpy(graph)
            algo_result = algo(np_graph, graph)
            (cover_group, removed_counter) = algo_result[0:2]
            cover_size = len(cover_group) + removed_counter
            results[algo.__name__].append(cover_size)
    result_list = [results[algo.__name__] for algo in algorithms] # 3 x iterations
    results_averaged = np.mean(result_list, axis=1)
    # results_alpha = results_averaged/n

    print(f'alpha for c: {c} is: {results_averaged}')
    return results_averaged


def main():
    n = 1000
    # step = 0.5
    # stop = 10
    #step = 100
    #stop = 100
    iterations = 100
    # algorithms = [xyz_v3_algo, xyz_v3_algo_with_reductions, novac1_algo, degree]
    algorithms = [xyz_v3_algo_without_reductions, xyz_v3_algo_only_with_leaf_parent_reduction]

    #algorithm = novac1_algo

    #lambda_array = np.linspace(step, stop, num=int(1/step*stop))
    #n_array = np.linspace(step, stop, num=int(1/step*stop))
    # lambda_array = [1.9]
    #results = [run_graph(algorithms, int(n), 1, iterations) for n in n_array]
    # results = [run_graph(algorithms, n, c, iterations) for c in lambda_array]
    results = run_graph(algorithms, n, c=1, iterations=iterations)
    print(results)

    #columns = [algo.__name__ for algo in algorithms]
    results = run_graph(algorithms, n, c=1, iterations=iterations)
    df = pd.DataFrame(results, index=[algo.__name__ for algo in algorithms])
    # df = pd.DataFrame(results, lambda_array, columns)
    #df = pd.DataFrame(results, n_array, columns)

    # df.to_csv(f'./compare-results-n{n}.csv')
    # df.to_csv(f'./compare-results-running_n.csv')
    df.to_csv(f'./compare-results-tree-n{n}.csv')


if __name__ == '__main__':
    main()