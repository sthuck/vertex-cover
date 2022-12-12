from igraph import Graph, Vertex
import random
from typing import Set, List


def flatten(t: List[List]):
    return [item for sublist in t for item in sublist]


def bwc_degree_algo(graph: Graph, initial_b: int):
    b = initial_b
    v: Vertex
    B: Set[Vertex] = set()

    current_degree = 0

    while b > 0:
        current_degree_vertices = [v for v in graph.vs if v.degree() == current_degree]
        how_many_to_color_black = b if b < len(current_degree_vertices) else len(current_degree_vertices)
        color_as_black = random.sample(current_degree_vertices, how_many_to_color_black)
        for v in color_as_black:
            B.add(v)
        b = b - len(color_as_black)
        current_degree += 1

    neighbors_of_blacks = set(flatten([v.neighbors() for v in B]))
    W = set(v for v in graph.vs if v not in neighbors_of_blacks and v not in B)

    return graph, W
