from bwc.bwc_degree import bwc_degree_algo
from bwc.bwc_algo import bwc_algo
from bwc.bwc import bwc_random_algo
from bwc.bwc_min import bwc_min_algo
import numpy as np
from igraph import Graph
from typing import List, Dict
import pandas as pd

def main():
    n = 1000
    initial_b = 250
    iteration = 100
    step = 0.1
    stop = 10
    algorithms = [bwc_algo, bwc_min_algo]
    # , bwc_algo, bwc_random_algo, bwc_min_algo, bwc_degree_algo,
    lambda_array = np.linspace(step, stop, num=int(1/step*stop))
    # (0...stop] -> in skips of step

    # [start..stop, total of num]

    c_results = {}
    for c in lambda_array:
        p = c / n
        graph: Graph = Graph.Erdos_Renyi(n=n, p=p)
        results: Dict[str, List[int]] = {algo.__name__: [] for algo in algorithms}
        for i in range(iteration):
            print(f'iteration {i}')
            for algo in algorithms:
                copy = graph.copy()
                _, W = algo(copy, initial_b)
                results[algo.__name__].append(len(W))
        df = pd.DataFrame(results)
        mean_series = df.mean()
        c_results[c] = mean_series
    df = pd.DataFrame(c_results)
    return df


if __name__ == '__main__':
    df = main()
    df.to_csv('./bwc_compare.csv')