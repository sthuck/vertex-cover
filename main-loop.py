from graph_utils import *
import time
from algorithms.shaked_algo import shaked_algo
from algorithms.vsa import vsa
from algorithms.vsa_by_min import vsa_by_min
from algorithms.degree import degree
from algorithms.shaked_algo_impl import shaked_algo_impl
from algorithms.xyz import xyz_algo
from algorithms.xyzV2 import xyz_v2_algo
from algorithms.first_vertex_with_degree import first_vertex_with_degree_algo
from algorithms.xyz_larger_diff import xyz_larger_diff_algo
from algorithms.neighbors_algo import neighbors_algo
from algorithms.most_neighbors_with_minimal_degree import most_neighbors_with_minimal_degree_algo


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Definitions
    n = 1000
    p = 2/1000
    e = 8
    iterations = 10
    # algorithms = [vsa, vsa_by_min, degree, shaked_algo, shaked_algo_impl, xyz_algo, xyz_v2_algo, xyz_larger_diff_algo, first_vertex_with_degree_algo, neighbors_algo]
    algorithms = [ xyz_algo, neighbors_algo, most_neighbors_with_minimal_degree_algo]

    # End Definitions
    results = {algo.__name__: np.zeros(iterations) for algo in algorithms}
    all_graph_stats = []

    for i in range(iterations):
        graph = random_graph(n, p)
        # graph = random_graph_by_edges(n, e)

        np_graph = graph_to_numpy(graph)

        stats = graph_stats(np_graph)
        stats.update({'Graph name': i, 'Edges Num': len(graph.es), 'Vertex Num': len(graph.vs)})
        stats.update({'parents of leaves': count_parents_of_leaves(graph)})

        print('iteration:', i, '   number of edges:', len(graph.es))
        for algorithm in algorithms:
            np_graph_copy = np.copy(np_graph)
            result = algorithm(np_graph_copy, graph)
            if isinstance(result, list):
                results[algorithm.__name__][i] = len(result)
                stats.update({algorithm.__name__: len(result)})
            else:  # for shaked algo
                results[algorithm.__name__][i] = result
                stats.update({'Sigma D(Vi)/D(Vi)+1': result})

        all_graph_stats.append(stats)

    for (algorithm_name, result_vector) in results.items():
        average = result_vector.sum()/iterations
        print(algorithm_name, ' has average: ', average)
    write_csv_stats(all_graph_stats)


if __name__ == '__main__':
    simple_becnh(main)
