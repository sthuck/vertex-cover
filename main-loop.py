from graph_utils import *
import time
from alogrithms.shaked_algo import shaked_algo
from alogrithms.vsa import vsa
from alogrithms.vsa_by_min import vsa_by_min
from alogrithms.degree import degree
from alogrithms.shaked_algo_impl import shaked_algo_impl
from alogrithms.xyz import xyz_algo
from alogrithms.xyzV2 import xyz_v2_algo


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Definitions
    n = 100
    p = 0.05
    e = 8
    iterations = 20
    # ALL: algorithms = [vsa, vsa_by_min, degree, shaked_algo, shaked_algo_impl]
    algorithms = [vsa, vsa_by_min, degree, shaked_algo, shaked_algo_impl, xyz_algo, xyz_v2_algo]

    # End Definitions
    results = {algo.__name__: np.zeros(iterations) for algo in algorithms}
    all_graph_stats = []

    for i in range(iterations):
        graph = random_graph(n, p)
        # graph = random_graph_by_edges(n, e)

        np_graph = graph_to_numpy(graph)

        stats = graph_stats(np_graph)
        stats.update({'Graph name': i, 'Edges Num': len(graph.es), 'Vertex Num': len(graph.vs)})

        print('iteration:', i, '   number of edges:', len(graph.es))
        for algorithm in algorithms:
            np_graph_copy = np.copy(np_graph)
            result = algorithm(np_graph_copy)
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
