from graph_utils import *
import time
import math
from algorithms.xyz import xyz_algo, xyz_v2_algo, xyz_v3_algo, xyz_weak_algo
from algorithms.neighbors_algo import neighbors_algo
from algorithms.most_neighbors_with_minimal_degree import most_neighbors_with_minimal_degree_algo
from algorithms.novac1 import novac1_algo
from algorithms.degree import degree
from algorithms.degree_minus import degree_minus
from algorithms.shaked_algo_impl_v2 import shaked_algo_impl_v2
from algorithms.g_of_v_algo import g_of_v_algo
from algorithms.g_of_v_algo import compute_g_of_v_for_testing_orig
import pandas as pd

# noinspection DuplicatedCode
def main():
    # Definitions
    n = 1000
    ps = [3/1000, 1/1000, 10/1000]
    results = []
    for p in ps:
        graph = random_graph(n, p)

        cover_group, _, (__, g_of_v_algo_cover_group_g_of_v) =\
            g_of_v_algo(None, graph)
        results.append(g_of_v_algo_cover_group_g_of_v)

    results_df = pd.DataFrame(results).T
    results_df.columns = ['G(1000,3/1000)', '1', '10']
    averaged_results_df = split_dataframe_to_averaged_bins(results_df, 25)
    averaged_results_df.plot(title='g_of_v algo, g_of_v_value per iteration')

    print('f')


if __name__ == '__main__':
    main()
