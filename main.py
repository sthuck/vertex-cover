from graph_utils import *
from vsa_sparse_v2 import vsa
import time


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    graph = random_graph(5000, 0.0005)
    np_graph = graph_to_numpy(graph)
    vertices = vsa(np_graph)
    # write_to_file('out.svg', graph, vertices)
    # write_to_graphml(graph, vertices)

    # print(vertices)
    print('length:', len(vertices))


if __name__ == '__main__':
    simple_becnh(main)
