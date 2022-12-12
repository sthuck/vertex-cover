from graph_utils import *

from bwc.bwc_degree import bwc_degree_algo
from bwc.bwc_algo import bwc_algo

from algorithms.g_of_v_algo import g_of_v_algo_bwc
from algorithms.g_of_v_algo import compute_g_of_v_for_testing_orig
import pandas as pd


# Definitions
n = 1000
p = 2/1000
b = 200

graph = random_graph(n, p)

cover_group, _, (bwc_algo, bwc_algo_cover_group_g_of_v) =\
    g_of_v_algo_bwc(None, graph)
print('======')
print(f'g_of_v_bwc algo total cover group: {len(cover_group)}')
cover_group, removed_counter, (bwc_degree_algo_cover_group_degree, bwc_degree_algo_cover_group_g_of_v) = bwc_degree_algo(None, graph)
print('======')
print(f'bwc_degree_algo algo total cover group: {len(cover_group)}')

bwc_algo_g_of_v_df = pd.DataFrame({'bwc_algo': bwc_algo_cover_group_g_of_v})
bwc_degree_g_of_v_df = pd.DataFrame({'bwc_degree': bwc_degree_algo_cover_group_g_of_v})



spacing_for_average = 100
averaged_bwc_algo_g_of_v_df = split_dataframe_to_averaged_bins(bwc_algo_g_of_v_df, spacing_for_average)
averaged_bwc_degree_g_of_v_df = split_dataframe_to_averaged_bins(bwc_degree_g_of_v_df, spacing_for_average)


#averaged_bwc_algo_g_of_v_df.plot(ax=ax1)
df3_averaged_bwc_degree_g_of_v_df_spacing = pd.DataFrame()
for i in range(len(averaged_bwc_degree_g_of_v_df)):
    jump = int((spacing_for_average*i) + (spacing_for_average/2))
    df3_averaged_bwc_degree_g_of_v_df_spacing.loc[jump, 'bwc_degree'] = averaged_bwc_degree_g_of_v_df.loc[i, 'bwc_degree']
    #
df3_averaged_bwc_algo_g_of_v_df_spacing = pd.DataFrame()
for i in range(len(averaged_bwc_algo_g_of_v_df)):
    jump = int((spacing_for_average*i) + (spacing_for_average/2))
    df3_averaged_bwc_algo_g_of_v_df_spacing.loc[jump, 'bwc_algo'] = averaged_bwc_algo_g_of_v_df.loc[i, 'bwc_algo']
    #

ax1 = df3_averaged_bwc_degree_g_of_v_df_spacing.plot(title='')
df3_averaged_bwc_algo_g_of_v_df_spacing.plot(ax=ax1)


g_of_v_algo_degree_df = pd.DataFrame({'bwc_algo': bwc_algo_cover_group_g_of_v})
g_of_v_algo_averaged_degree_df = split_dataframe_to_averaged_bins(g_of_v_algo_degree_df, spacing_for_average)
# newx = np.linspace(0, 1, len(g_of_v_algo_averaged_degree_df))
# g_of_v_algo_averaged_degree_df.index = newx

degree_algo_degree_df = pd.DataFrame({'bwc_degree': bwc_degree_algo_cover_group_g_of_v})
# degree_algo_averaged_degree_df = split_dataframe_to_averaged_bins(degree_algo_degree_df, 1)

 #newx = np.linspace(0, 1, len(degree_algo_degree_df))
 #degree_algo_degree_df.index = newx

ax1 = degree_algo_degree_df.plot(title='')
#g_of_v_algo_averaged_degree_df.plot(ax=ax1)
df3_g_of_v_algo_averaged_degree_spacing = pd.DataFrame()
for i in range(len(g_of_v_algo_averaged_degree_df)):
    jump = int((spacing_for_average*i) + (spacing_for_average/2))
    df3_g_of_v_algo_averaged_degree_spacing.loc[jump, 'bwc_algo'] = g_of_v_algo_averaged_degree_df.loc[i, 'bwc_algo']
    #


df3_g_of_v_algo_averaged_degree_spacing.plot(ax=ax1)
#a =1