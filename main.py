from graph_utils import *
from algorithms.xyz import xyz_v2_algo, xyz_v3_algo
import time


def simple_bench(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Definition
    n = 100
    p = 0.15
    # All options: vsa, vsa_by_min, shaked_algo, degree
    algorithm = xyz_v3_algo

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
        print('xyz_v3_algo:', len(result[0]) + result[1])
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
