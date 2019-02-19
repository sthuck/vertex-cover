from graph_utils import *
from alogrithms.vsa import vsa
from alogrithms.vsa_by_min import vsa_by_min
from alogrithms.shaked_algo import shaked_algo
from alogrithms.degree import degree
from alogrithms.xyzV2 import xyz_v2_algo
import time


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Definition
    n = 20
    p = 0.2
    # All options: vsa, vsa_by_min, shaked_algo, degree
    algorithm = xyz_v2_algo

    # random graph:
    graph = random_graph(n, p)
    np_graph = graph_to_numpy(graph)

    # read dimacs:
    # (graph, np_graph) = read_dimacs('./example-graph/brock200_4.clq')

    # Algorithm
    result = algorithm(np_graph)

    if algorithm.__name__ == 'shaked_algo':
        print('shaked_algo, E:', result)
    else:
        vertices = result
        write_to_file('out.svg', graph, vertices)
        write_to_graphml(graph, vertices)

        print(vertices)
        print('length:', len(vertices))


if __name__ == '__main__':
    simple_becnh(main)
