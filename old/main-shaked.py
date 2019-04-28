from graph_utils import *
import time
from algorithms.shaked_algo import shaked_algo


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Input

    # random graph:
    graph = random_graph(5, 0.5)
    np_graph = graph_to_numpy(graph)

    # read last graph
    # graph = igraph.Graph.Read_GraphML('output.graphml', False)
    # np_graph = graph_to_numpy(graph)


    # read dimacs:
    # (graph, np_graph) = read_dimacs('./example-graph/johnson8-2-4.clq')
    result = shaked_algo(np_graph)
    print('result:', result)
    graph.write('output.graphml', format='graphml')



if __name__ == '__main__':
    simple_becnh(main)
