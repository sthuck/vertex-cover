
from igraph import Graph, Vertex
import pandas as pd
from enum import Enum
import random


class Color(Enum):
    BLACK = 1
    WHITE = 2
    UNCOLORED = 3


def is_neighbor_of_black(vertex: Vertex):
    neighbors = vertex.neighbors()
    for n in neighbors:
        if n['color'] == Color.BLACK:
            return True
    return False


def count_white(g: Graph):
    return sum([1 for v in g.vs if v['color'] == Color.WHITE])


def do_iteration(g: Graph, n: int):
    black_vertices = set(random.sample(range(n), b))
    vertex: Vertex
    for vertex in g.vs:
        vertex['color'] = Color.BLACK if vertex.index in black_vertices else Color.UNCOLORED

    for vertex in filter(lambda v: v['color'] != Color.BLACK, g.vs):
        if not is_neighbor_of_black(vertex):
            vertex['color'] = Color.WHITE

    return count_white(g)


if __name__ == '__main__':
    n = 3
    m = 2
    graph: Graph = Graph.Erdos_Renyi(n=n, m=m)
    iterations = 1000
    b = 2

    results = []
    i = 0
    for _ in range(iterations):
        i += 1
        if i % 10 == 0:
            print(f'iteration {i}')
        g: Graph = graph.copy()
        result = do_iteration(g, n)
        results.append(result)

    results_series = pd.Series(results)
    print(f'mean: {results_series.mean()}, variance: {results_series.var()}')





