from algorithms import shaked_algo_impl
from graph_utils import  graph_to_numpy
from igraph import Graph
import numpy as np


def main():
    iterations = 100
    n = 1000
    c = 1
    results = []
    for i in range(iterations):
        graph: Graph = Graph.Erdos_Renyi(n, c / n)
        np_graph = graph_to_numpy(graph)
        cover_group = shaked_algo_impl.shaked_algo_impl(np_graph)
        cover_group_size = len(cover_group)
        print(f'iteration {i}: {cover_group_size}')
        results.append(cover_group_size)
    print('=========')
    avg = np.array(results).mean()
    print(f'average: {avg}')
    variance = np.array(results).var()
    print(f'variance: {variance}')


if __name__ == '__main__':
    main()