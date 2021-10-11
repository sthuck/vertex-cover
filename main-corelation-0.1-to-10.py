from g_of_v.g_of_v import compute_g_of_v
from graph_utils import *
from algorithms.xyz import xyz_v2_algo, xyz_v3_algo
from algorithms.novac1 import novac1_algo
from algorithms.degree import degree
import time
import numpy as np
import pandas as pd


# returns list 3 items
def run_graph(n, c, iterations=20):
    print(f'running for c value: {c}')
    results = []
    for i in range(iterations):
        p = c / n
        graph = random_graph(n, p)
        degree_vector = [v.degree() for v in graph.vs]
        g_vector = [compute_g_of_v(v) for v in graph.vs]
        corelation = np.corrcoef(degree_vector, g_vector)[0][1]
        results.append(corelation)
    return np.mean(results)


def main():
    n = 10000
    step = 0.1
    stop = 10
    iterations = 20


    lambda_array = np.linspace(step, stop, num=int(1/step*stop))
    results = [run_graph(n, c, iterations) for c in lambda_array]
    df = pd.DataFrame(results, lambda_array)
    return df


if __name__ == '__main__':
    df = main()
    df.plot()
    df.to_csv("output.correlation.csv")
    # df.to_csv(f'./compare-results-n{n}.csv')


