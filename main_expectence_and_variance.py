from graph_utils import *
import time
import numpy
from algorithms.shaked_algo_impl import shaked_algo_impl
from algorithms.shaked_algo_impl_randomized import shaked_algo_impl_randomized

def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


# noinspection DuplicatedCode
def main():
    # Definitions
    n = 1000
    p = 3/1000
    e = 8
    iterations = 1000

    print('Phase 1 - same graph, random index choose')
    graph = random_graph(n, p)
    np_graph = graph_to_numpy(graph)
    results_phase_1 = []

    for i in range(iterations):
        print('phase 1, iteration', i)
        copy = np_graph.copy()
        cover_group = shaked_algo_impl_randomized(copy)
        results_phase_1.append(len(cover_group))

    print('Phase 2 - random graph, choose index by order')
    results_phase_2 = []
    for i in range(iterations):
        print('phase 2, iteration', i)
        graph = random_graph(n, p)
        np_graph = graph_to_numpy(graph)
        cover_group = shaked_algo_impl(np_graph)
        results_phase_2.append(len(cover_group))

    print(results_phase_1)
    print('phase 1 avg: ', numpy.mean(numpy.array(results_phase_1)))
    print('phase 1 variance: ', numpy.var(numpy.array(results_phase_1)))

    print(results_phase_2)
    print('phase 2 avg: ', numpy.mean(numpy.array(results_phase_2)))
    print('phase 2 variance: ', numpy.var(numpy.array(results_phase_2)))



if __name__ == '__main__':
    simple_becnh(main)
