from graph_utils import *
from algorithms.xyz import xyz_v2_algo, xyz_v3_algo
from algorithms.novac1 import novac1_algo
import time
import numpy as np
import pandas as pd


def run_graph(n, c) -> int:
    # print(f'running for c value: {c}')
    p = c / n
    graph = random_graph(n, p)
    (cover_group, removed_counter ) = xyz_v3_algo(None, graph)
    cover_size = len(cover_group) + removed_counter
    print(f'alpha for c: {c} is: {cover_size/n}')
    return cover_size/n


def main():
    n = 10000
    lambda_array = np.linspace(0.1, 5)
    results = [run_graph(n, c) for c in lambda_array]
    df = pd.DataFrame(results, lambda_array)
    df.to_csv('./xyz3-results.csv')


if __name__ == '__main__':
    main()