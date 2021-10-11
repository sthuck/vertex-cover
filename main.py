from graph_utils import *
from algorithms.xyz import xyz_v2_algo, xyz_v3_algo
from algorithms.novac1 import novac1_algo
from algorithms.degree_minus import degree_minus
from algorithms.shaked_algo_impl_v2 import shaked_algo_impl_v2
import time


def simple_bench(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Definition
    n = 100
    c = 2
    p = c / n
    # All options: vsa, vsa_by_min, shaked_algo_impl_v2, degree, degree_minus
    algorithms = [novac1_algo, xyz_v3_algo]

    # random graph:
    orig = random_graph(n, p)
    np_orig = graph_to_numpy(orig)
    # read dimacs:
    # (orig, np_orig) = read_dimacs('./example-graph/johnson8-2-4.clq', reverse=True)

    for algorithm in algorithms:
        graph = orig.copy()
        np_graph = np_orig.copy()

        print('Number of parents of leaves', count_parents_of_leaves(graph))
        # Algorithm
        result = algorithm(np_graph, graph)

        if algorithm.__name__ == 'shaked_algo':
            print('shaked_algo, E:', result)
        elif algorithm.__name__ == 'xyz_weak_algo':
            print('xyz_weak_algo:', len(result[0]) + result[1])
        elif algorithm.__name__ == 'degree':
            print('degree:', len(result[0]) + result[1])
        else:
            vertices = result[0] if type(result) == tuple else result
            write_to_file(f'out-{algorithm.__name__}.svg', graph, vertices)
            write_to_graphml(graph, vertices, f'out-{algorithm.__name__}')

            print(vertices)
            print('vertex cover length:', len(vertices))
            # is_legal = check_if_legal_vertex_cover(graph_to_numpy(graph), result)
            # print('Checking if we got a valid vertex cover...', 'YES' if is_legal else 'NO')


if __name__ == '__main__':
    simple_bench(main)
