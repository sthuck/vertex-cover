from algorithms.xyz import xyz_v3_algo_with_reductions
from graph_utils import random_graph, graph_to_numpy
from algorithms.reductions import ReductionCounters
import pandas as pd
import numpy as np
n = 1000
p = 2/1000
step=0.5
stop=2
iterations = 1
lambda_array = np.linspace(step, stop, num=int(1 / step * stop))

total_stats_reduce_1_only = {'cover_size': [], 'removed_in_reductions': [], 'removed first iteration reduction1':[]}
total_stats_reduce_1_and_2 = {'cover_size': [], 'removed_in_reductions': [], 'removed first iteration reduction1':[]}
args_reduce_1_only = {'do_reduce_1': True, 'do_reduce_2': False, 'do_reduce_3': False}
args_reduce_1_and_2 = {'do_reduce_1': True, 'do_reduce_2': True, 'do_reduce_3': False}

for i in range(iterations):
    print(f'iteration {i}:')
    orig = random_graph(n, p)

    for (stats, args) in [(total_stats_reduce_1_only, args_reduce_1_only), (total_stats_reduce_1_and_2, args_reduce_1_and_2)]:
        graph = orig.copy()

        cover_group, removed_counter, *extra = xyz_v3_algo_with_reductions(None, graph, **args)
        xyz3_metadata = extra[0]
        stats['cover_size'].append(len(cover_group) + removed_counter)
        reduction_counters: ReductionCounters = xyz3_metadata['reduction_counters']
        stats['removed_in_reductions'].append(reduction_counters.reduction_1_counter +
                                                                  reduction_counters.reduction_2_counter)
        stats['removed first iteration reduction1'].append(xyz3_metadata['removed_in_first_reduction_first_iteration'])

print('====== Reduction 1 Only ======= ')
df1 = pd.DataFrame(total_stats_reduce_1_only)
print(df1)

print('====== Reduction 1 and 2 ======= ')
df2 = pd.DataFrame(total_stats_reduce_1_and_2)
print(df2)





