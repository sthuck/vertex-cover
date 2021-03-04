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
    p = 3/1000

    graph = random_graph(n, p)

    cover_group, _, (g_of_v_algo_cover_group_degree, g_of_v_algo_cover_group_g_of_v) =\
        g_of_v_algo(None, graph)
    print('======')
    print(f'g_of_v algo total cover group: {len(cover_group)}')
    cover_group, removed_counter, (cover_group_algo_cover_group_degree,) = degree(None, graph)
    print('======')
    print(f'degree algo total cover group: {len(cover_group)}')

    g_of_v_df = pd.DataFrame({'g of v': g_of_v_algo_cover_group_g_of_v})
    averaged_g_of_v_df = split_dataframe_to_averaged_bins(g_of_v_df, 1)
    averaged_g_of_v_df.plot(title='g_of_v algo, g_of_v_value per iteration')

    g_of_v_algo_degree_df = pd.DataFrame({'g-of-v degree': g_of_v_algo_cover_group_degree})
    g_of_v_algo_averaged_degree_df = split_dataframe_to_averaged_bins(g_of_v_algo_degree_df, 1)

    degree_algo_degree_df = pd.DataFrame({'degree algo degree': cover_group_algo_cover_group_degree})
    degree_algo_averaged_degree_df = split_dataframe_to_averaged_bins(degree_algo_degree_df, 1)

    ax1 = degree_algo_averaged_degree_df.plot(title='change me')
    g_of_v_algo_averaged_degree_df.plot(ax=ax1)


if __name__ == '__main__':
    main()
