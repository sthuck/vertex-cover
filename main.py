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
    n = 2000
    c = 5
    p = c/n
    # All options: vsa, vsa_by_min, shaked_algo_impl_v2, degree, degree_minus
    algorithm = degree_minus

    # random graph:
    graph = random_graph(n, p)
    np_graph = graph_to_numpy(graph)

    # read dimacs:
    # (graph, np_graph) = read_dimacs('./example-graph/johnson8-2-4.clq', reverse=True)

    print('Number of parents of leaves', count_parents_of_leaves(graph))
    # Algorithm
    result = algorithm(np_graph, graph)

    if algorithm.__name__ == 'shaked_algo':
        print('shaked_algo, E:', result)
    elif algorithm.__name__ == 'xyz_v3_algo':
        print('xyz_v3_algo:', len(result[0]) + result[1])
    elif algorithm.__name__ == 'xyz_weak_algo':
        print('xyz_weak_algo:', len(result[0]) + result[1])
    elif algorithm.__name__ == 'novac1_algo':
        print('novac1_algo:', len(result[0]) + result[1])
    elif algorithm.__name__ == 'degree':
        print('degree:', len(result[0]) + result[1])
    else:
        vertices = result
        write_to_file('out.svg', graph, vertices)
        write_to_graphml(graph, vertices)

        print(vertices)
        print('length:', len(vertices))
        is_legal = check_if_legal_vertex_cover(graph_to_numpy(graph), result)
        print('Checking if we got a valid vertex cover...', 'YES' if is_legal else 'NO')


if __name__ == '__main__':
    simple_bench(main)
