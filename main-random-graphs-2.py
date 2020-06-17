from algorithms import shaked_algo_impl
from algorithms import shaked_algo_impl_v2
from graph_utils import graph_to_numpy
from igraph import Graph
import numpy as np
import matplotlib.pyplot as plt


def main():
    iterations = 100000
    n = 1000
    c = 1
    results = []
    rhs_a = (n / c) * (c - 1 + np.e ** (-c))
    rhs_b = (n / (2 * c)) * (np.e ** (-c) - 1) ** 2

    numerator = rhs_a
    denominator = np.sqrt(rhs_b)

    for i in range(iterations):
        graph: Graph = Graph.Erdos_Renyi(n, c / n)
        np_graph = graph_to_numpy(graph)
        cover_group = shaked_algo_impl_v2.shaked_algo_impl_v2(np_graph)
        cover_group_size = len(cover_group)
        if i % 100 == 0:
            print(f'iteration {i}: {cover_group_size}')
        results.append(cover_group_size)
    theorem2_c = (np.array(results) - numerator)/denominator
    print('=========')
    avg = np.array(results).mean()
    print(f'average: {avg}')
    print(f'rhs_a {rhs_a}')

    variance = np.array(results).var()
    print(f'variance: {variance}')
    print(f'rhs_b {rhs_b}')
    np.save('theorem2_c.npy', theorem2_c)
    plot_hist(theorem2_c)


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


