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


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


# noinspection DuplicatedCode
def main():
    # Definitions
    n = 1000
    p = 10/1000
    e = 8

    iterations = 1
    # algorithms = [vsa, vsa_by_min, degree, shaked_algo, shaked_algo_impl, xyz_algo, xyz_v2_algo, xyz_larger_diff_algo, first_vertex_with_degree_algo, neighbors_algo]
    algorithms = [g_of_v_algo, degree]

    # End Definitions
    results = {algo.__name__: np.zeros(iterations) for algo in algorithms}
    all_graph_stats = []

    for i in range(iterations):
        print('==')
        graph = random_graph(n, p)
        # graph = random_graph_by_edges(n, e)
        df1 = pd.DataFrame(data=compute_g_of_v_for_testing_orig(graph))
        a = df1[0].var()
        b = df1[2].mean()
        print(f'Coefficient of correlation  {b * (1/(math.sqrt(a*n*p)))}')
        np_graph = graph_to_numpy(graph)
        stats = graph_stats(np_graph)
        stats.update({'Graph name': i, 'Edges Num': len(graph.es), 'Vertex Num': len(graph.vs)})
        stats.update({'parents of leaves': count_parents_of_leaves(graph)})

        print('main loop:: iteration:', i, '   number of edges:', len(graph.es))
        for algorithm in algorithms:
            np_graph_copy = np.copy(np_graph)
            result = algorithm(np_graph_copy, graph)

            if any(name == algorithm.__name__ for name in ['g_of_v_algo', 'xyz_v3_algo', 'xyz_weak_algo', 'novac1_algo', 'degree']):
                print(algorithm.__name__, '::', len(result[0]) + result[1])
                results[algorithm.__name__][i] = len(result[0]) + result[1]
                stats.update({algorithm.__name__: len(result[0]) + result[1]})

            elif algorithm.__name__ == 'shaked_algo':
                print(algorithm.__name__, '::', result)
                results[algorithm.__name__][i] = result
                stats.update({'Sigma D(Vi)/D(Vi)+1': result})

            else:
                print(algorithm.__name__, '::', len(result))
                results[algorithm.__name__][i] = len(result)
                stats.update({algorithm.__name__: len(result)})

            if hasattr(algorithm, 'extra_metadata'):
                algorithm.extra_metadata(result[2])

        all_graph_stats.append(stats)

    for (algorithm_name, result_vector) in results.items():
        average = result_vector.sum()/iterations
        print(algorithm_name, ' has average: ', average)
    write_csv_stats(all_graph_stats)


if __name__ == '__main__':
    simple_becnh(main)
