from algorithms import shaked_algo_impl
from algorithms import shaked_algo_impl_v2
from graph_utils import graph_to_numpy
from igraph import Graph
import numpy as np
import matplotlib.pyplot as plt


def main():
    what_graph = 'gnp'  # gnp | star | ring
    iterations = 50
    n = 1000
    c = 2.75
    results = []
    if what_graph == 'gnp':
        rhs_a = (n / c) * (c - 1 + np.e ** (-c))
        rhs_b = (n / (2 * c)) * (np.e ** (-c) - 1) ** 2

        numerator = rhs_a
        denominator = np.sqrt(rhs_b)

    for i in range(iterations):

        if what_graph == 'gnp':
            graph: Graph = Graph.Erdos_Renyi(n, c / n)
            randomize = False
        elif what_graph == 'ring':
            graph: Graph = Graph.Ring(n)
            randomize = True
        elif what_graph == 'star':
            graph: Graph = Graph.Star(n)
            randomize = True
        else:
            raise Exception("Bad what_graph value")

        np_graph = graph_to_numpy(graph)
        cover_group = shaked_algo_impl_v2.shaked_algo_impl_v2(np_graph, randomize=randomize)
        cover_group_size = len(cover_group)
        if i % 100 == 0:
            print(f'iteration {i}')
        results.append(cover_group_size)
    if what_graph == 'gnp':
        theorem2_c = (np.array(results) - numerator)/denominator

    print('=========')
    avg = np.array(results).mean()
    print(f'average: {avg}')

    if what_graph == 'gnp':
        print(f'rhs_a {rhs_a}')

    variance = np.array(results).var()
    print(f'variance: {variance}')

    if what_graph == 'gnp':
        print(f'rhs_b {rhs_b}')
        np.save('theorem2_c.npy', theorem2_c)
        plot_hist(theorem2_c)

    if what_graph == 'star':
        expectation = (n**2 + n-2)/(2*n)
        print(f'star expectation: {expectation}')


def plot_hist(x):
    num_bins = 50

    mu = 0  # mean of distribution
    sigma = 1  # standard deviation of distribution

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=1)

    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
    ax.plot(bins, y, '--')
    ax.set_xlabel('')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Theorem 2c')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
     main()


### TODO:
# n=1000 iterations = 100,000 c=1
# n=1000 iterations= 1,000,000 c=0.5
# n=1000 iterations= 1,000,000 c=0.25
# ring graph n = 1000, iterations=100,000
# star graph n = 1000, iterations=100,000
