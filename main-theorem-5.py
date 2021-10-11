from algorithms import shaked_algo_impl
from algorithms import shaked_algo_impl_v2
from graph_utils import graph_to_numpy
from igraph import Graph
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

def main():
    iterations = 1000000
    n = 1000
    c = 1
    results = []

    graph: Graph = Graph.Erdos_Renyi(n, c / n)
    randomize = True

    for i in range(iterations):
        np_graph = graph_to_numpy(graph)

        cover_group = shaked_algo_impl_v2.shaked_algo_impl_v2(np_graph, randomize=randomize)
        cover_group_size = len(cover_group)
        if i % 100 == 0:
            print(f'iteration {i}')
        results.append(cover_group_size)
    results = np.array(results)
    print('=========')
    avg = results.mean()
    print(f'average: {avg}')

    variance = results.var()
    print(f'variance: {variance}')
    np.save('theorem5.npy', results)
    bins = np.max(results)-np.min(results)
    results = (results - avg)/np.sqrt(variance)
    plot_hist(results, bins)

    return results


def plot_hist(x, num_bins=50):

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
    ax.set_title(r'')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
     raw_results = main()


### TODO:
# n=1000 iterations = 100,000 c=1
# n=1000 iterations= 1,000,000 c=0.5
# n=1000 iterations= 1,000,000 c=0.25
# ring graph n = 1000, iterations=100,000
# star graph n = 1000, iterations=100,000
