from graph_utils import *
from plot_theorem2c import plot_density, plot_hist
from g_of_v import compute_g_of_v


def main():
    # Definition
    n = 1000
    p = 0.003


    # random graph:
    graph: Graph = random_graph(n, p)
    x = [compute_g_of_v(v) for v in graph.vs]
    print(x)
    plot_density(x)
    plot_hist(x, 'g of v', 100, False)


if __name__ == '__main__':
    main()
