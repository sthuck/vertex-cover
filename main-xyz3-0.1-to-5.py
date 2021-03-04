from graph_utils import *
from algorithms.xyz import xyz_v2_algo, xyz_v3_algo
from algorithms.novac1 import novac1_algo
from algorithms.degree import degree
import time
import numpy as np
import pandas as pd


# returns list 3 items
def run_graph(algorithms, n, c, iterations=20) -> int:
    # print(running for c value: {c}')
    results = {algo.__name__: [] for algo in algorithms}
    for i in range(iterations):
        p = c / n
        orig = random_graph(n, p)
        for algo in algorithms:
            graph = orig.copy()
            np_graph = graph_to_numpy(graph)
            algo_result = algo(np_graph, graph)
            (cover_group, removed_counter) = algo_result[0:2]
            cover_size = len(cover_group) + removed_counter
            results[algo.__name__].append(cover_size)
    result_list = [results[algo.__name__] for algo in algorithms] # 3 x iterations
    results_averaged = np.mean(result_list, axis=1)
    results_alpha = results_averaged/n

    print(f'alpha for c: {c} is: {results_alpha}')
    return results_alpha


def main():
    n = 1000
    step = 0.1
    stop = 10
    iterations = 100
    algorithms = [xyz_v3_algo, novac1_algo, degree]
    #algorithm = novac1_algo

    lambda_array = np.linspace(step, stop, num=int(1/step*stop))
    results = [run_graph(algorithms, n, c, iterations) for c in lambda_array]
    columns = [algo.__name__ for algo in algorithms]
    df = pd.DataFrame(results, lambda_array, columns)
    df.to_csv(f'./compare-results-n{n}.csv')


if __name__ == '__main__':
    main()