
from igraph import Graph, Vertex
import pandas as pd
from enum import Enum
import random


class Color(Enum):
    BLACK = '#000000'
    WHITE = '#ffffff'
    UNCOLORED = '#787b80'


def is_neighbor_of_black(vertex: Vertex):
    neighbors = vertex.neighbors()
    for n in neighbors:
        if n['color'] == Color.BLACK:
            return True
    return False


def bwc_random_algo(g: Graph, b: int):
    n = len(g.vs)
    black_vertices = set(random.sample(range(n), b))
    vertex: Vertex
    for vertex in g.vs:
        vertex['color'] = Color.BLACK if vertex.index in black_vertices else Color.UNCOLORED

    for vertex in filter(lambda v: v['color'] != Color.BLACK, g.vs):
        if not is_neighbor_of_black(vertex):
            vertex['color'] = Color.WHITE

    W = set(v for v in g.vs if v['color'] == Color.WHITE)

    return g, W


def do_iteration(g: Graph, b: int, iteration_num):
    g, C = bwc_random_algo(g, b)

    if iteration_num == 1:
        print([v['color'] for v in g.vs ])
        g_colored = g.copy()
        for v in g.vs:
            v['color'] = v['color'].value
        with open('bwc_after_coloring.svg', 'w') as f:
            g_colored.write_svg(f)

    return len(C)


if __name__ == '__main__':
    n = 4
    m = 20
    #graph: Graph = Graph.Erdos_Renyi(n=n, m=m)
    graph = Graph.Ring(n, circular=False)

    with open('bwc.svg', 'w') as f:
        graph.write_svg(f)

    iterations = 1000
    b = 2

    results = []
    i = 0
    for _ in range(iterations):
        i += 1
        if i % 10 == 0:
            print(f'iteration {i}')
        g: Graph = graph.copy()
        result = do_iteration(g, b, i)
        results.append(result)

    results_series = pd.Series(results)
    print(f'mean: {results_series.mean()}, variance: {results_series.var()}')





