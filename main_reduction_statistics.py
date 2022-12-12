from algorithms.novac1 import novac1_algo
from algorithms.xyz import xyz_v3_algo_with_reductions, xyz_v3_algo_without_reductions
from algorithms.degree import degree
from graph_utils import random_graph, graph_to_numpy
from algorithms.reductions import ReductionCounters
import pandas as pd
import numpy as np

def stand_alone_run():
    n = 10000
    start = 2.65
    step = 0.01
    stop = 2.65
    iterations = 1
    lambda_array = np.arange(start, stop + step, step)
   #algorithms = [degree]

    reductions_total_results = pd.DataFrame({})
   #algorithms_total_results = []

    for c in lambda_array:
        p = c / n

        total_stats_reduce_1_only = {'cover_size': [], 'removed_in_reductions': [], 'removed first iteration reduction1': []}
        total_stats_reduce_1_and_3 = {'cover_size': [], 'removed_in_reductions': [], 'removed first iteration reduction1': []}
      # total_stats_reduce_1_and_3_and_2 = {'cover_size': [], 'removed_in_reductions': [], 'removed first iteration reduction1': []}
        total_stats_reduce_1_and_2 = {'cover_size': [], 'removed_in_reductions': [], 'removed first iteration reduction1':[]}
        args_reduce_1_only = {'do_reduce_1': True, 'do_reduce_2': False, 'do_reduce_3': False}
        args_reduce_1_and_3 = {'do_reduce_1': True, 'do_reduce_2': False, 'do_reduce_3': True}
       # args_reduce_1_and_3_and_2 = {'do_reduce_1': True, 'do_reduce_3': True, 'do_reduce_2': True}
        args_reduce_1_and_2 = {'do_reduce_1': True, 'do_reduce_2': True, 'do_reduce_3': False}

       # algorithms_results = {algo.__name__: [] for algo in algorithms}

        for i in range(iterations):
            print(f'c: {c}, iteration {i}:')
            orig = random_graph(n, p)

           # for algo in algorithms:
            #    graph = orig.copy()
            #   np_graph = graph_to_numpy(graph)
            #    algo_result = algo(np_graph, graph)
            #    (cover_group, removed_counter) = algo_result[0:2]
            #    cover_size = len(cover_group) + removed_counter
            #   algorithms_results[algo.__name__].append(cover_size)

            for (stats, args) in [(total_stats_reduce_1_and_3, args_reduce_1_and_3),]:
                graph = orig.copy()

                cover_group, removed_counter, *extra = xyz_v3_algo_with_reductions(None, graph, **args)
                xyz3_metadata = extra[0]
                stats['cover_size'].append(len(cover_group) + removed_counter)
                reduction_counters: ReductionCounters = xyz3_metadata['reduction_counters']
                stats['removed_in_reductions'].append(reduction_counters.reduction_1_counter +
                                                                          reduction_counters.reduction_2_counter)
                stats['removed first iteration reduction1'].append(xyz3_metadata['removed_in_first_reduction_first_iteration'])

        df1 = pd.DataFrame(total_stats_reduce_1_and_3)
        m1 = df1.mean()
        m1 = m1.rename({k: f'r1+r4:{k}' for k in m1.index})

       # df2 = pd.DataFrame(total_stats_reduce_1_and_3_and_2)
       # m2 = df2.mean()
       # m2 = m2.rename({k: f'r1+r4+r2:{k}' for k in m2.index})
        series = pd.concat([m1])
        reductions_total_results.insert(len(reductions_total_results.columns), c, series)

      #  algorithms_results = [algorithms_results[algo.__name__] for algo in algorithms]  # 3 x iterations
      #  results_averaged = np.mean(algorithms_results, axis=1)
      #  algorithms_total_results.append(results_averaged)

   # columns = [algo.__name__ for algo in algorithms]
   # algorithms_total_results_df = pd.DataFrame(algorithms_total_results, lambda_array, columns)

    print(reductions_total_results)
    reductions_total_results.to_csv('main_reduction_statistics.csv')
   # algorithms_total_results_df.to_csv('main_reduction_statistics_algorithm_random_graph.csv')


#def was_called(_, orig: Graph,n,stop,start):

#    return
if __name__ == "__main__":
    stand_alone_run()