from igraph import Graph
from bwc.bwc_algo import bwc_algo
from bwc.king_graph import king_graph, rook_graph


def main():
    n = 1000
    c = 7
    p = c / n
    initial_b = 20

    graph: Graph = Graph.Erdos_Renyi(n=n, p=p)
    graph = king_graph(n=15, m=11)
    #graph = rook_graph(n=15, m=10)


    graph, W = bwc_algo(graph, initial_b)

    print(f'n={len(graph.vs)}')
    print(f'C = {len(graph.vs) - len(W)}')
    print(f'W = {len(W)}')



if __name__ == '__main__':
    main()