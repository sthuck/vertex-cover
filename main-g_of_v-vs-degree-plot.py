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


    # Definitions
n = 1000
p = 2/1000

graph = random_graph(n, p)

cover_group, _, (GEA_cover_group_degree, GEA_cover_group_g_of_v) =\
    g_of_v_algo(None, graph)
print('======')
print(f'g_of_v algo total cover group: {len(cover_group)}')
cover_group, removed_counter, (MDG_cover_group_degree, MDG_cover_group_g_of_v) = degree(None, graph)
print('======')
print(f'degree algo total cover group: {len(cover_group)}')

GEA_g_of_v_df = pd.DataFrame({'GEA': GEA_cover_group_g_of_v})
MDG_g_of_v_df = pd.DataFrame({'MDG': MDG_cover_group_g_of_v})



spacing_for_average = 100
averaged_GEA_g_of_v_df = split_dataframe_to_averaged_bins(GEA_g_of_v_df, spacing_for_average)
averaged_MDG_g_of_v_df = split_dataframe_to_averaged_bins(MDG_g_of_v_df, spacing_for_average)


#averaged_GEA_g_of_v_df.plot(ax=ax1)
df3_averaged_MDG_g_of_v_df_spacing = pd.DataFrame()
for i in range(len(averaged_MDG_g_of_v_df)):
    jump = int((spacing_for_average*i) + (spacing_for_average/2))
    df3_averaged_MDG_g_of_v_df_spacing.loc[jump, 'MDG'] = averaged_MDG_g_of_v_df.loc[i, 'MDG']
    #
df3_averaged_GEA_g_of_v_df_spacing = pd.DataFrame()
for i in range(len(averaged_GEA_g_of_v_df)):
    jump = int((spacing_for_average*i) + (spacing_for_average/2))
    df3_averaged_GEA_g_of_v_df_spacing.loc[jump, 'GEA'] = averaged_GEA_g_of_v_df.loc[i, 'GEA']
    #

ax1 = df3_averaged_MDG_g_of_v_df_spacing.plot(title='')
df3_averaged_GEA_g_of_v_df_spacing.plot(ax=ax1)


g_of_v_algo_degree_df = pd.DataFrame({'GEA': GEA_cover_group_degree})
g_of_v_algo_averaged_degree_df = split_dataframe_to_averaged_bins(g_of_v_algo_degree_df, spacing_for_average)
# newx = np.linspace(0, 1, len(g_of_v_algo_averaged_degree_df))
# g_of_v_algo_averaged_degree_df.index = newx

degree_algo_degree_df = pd.DataFrame({'MDG': MDG_cover_group_degree})
# degree_algo_averaged_degree_df = split_dataframe_to_averaged_bins(degree_algo_degree_df, 1)

 #newx = np.linspace(0, 1, len(degree_algo_degree_df))
 #degree_algo_degree_df.index = newx

ax1 = degree_algo_degree_df.plot(title='')
#g_of_v_algo_averaged_degree_df.plot(ax=ax1)
df3_g_of_v_algo_averaged_degree_spacing = pd.DataFrame()
for i in range(len(g_of_v_algo_averaged_degree_df)):
    jump = int((spacing_for_average*i) + (spacing_for_average/2))
    df3_g_of_v_algo_averaged_degree_spacing.loc[jump, 'GEA'] = g_of_v_algo_averaged_degree_df.loc[i, 'GEA']
    #


df3_g_of_v_algo_averaged_degree_spacing.plot(ax=ax1)
#a =1