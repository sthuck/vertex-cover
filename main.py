from graph_utils import *
from vsa import vsa
import time


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Input

    # random graph:
    # graph = random_graph(10, 0.5)
    # np_graph = graph_to_numpy(graph)

    # read dimacs:
    (graph, np_graph) = read_dimacs('./example-graph/brock200_1.clq')
    # Algorithm
    vertices = vsa(np_graph)

    # Output
    # write_to_file('out.svg', graph, vertices)
    # write_to_graphml(graph, vertices)

    # print(vertices)
    print('length:', len(vertices))


if __name__ == '__main__':
    simple_becnh(main)
