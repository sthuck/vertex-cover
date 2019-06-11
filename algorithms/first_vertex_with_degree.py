from igraph import Graph, Vertex
from typing import List


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def find_vertex_with_neighbours(graph: Graph) -> Vertex:
    return next(v for v in graph.vs if v.outdegree() > 0)


def select_vertices(graph: Graph) -> List[int]:
    return [v['name'] for v in find_vertex_with_neighbours(graph).neighbors()]


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def set_name(graph: Graph):
    for v in graph.vs:
        v['name'] = v.index


def first_vertex_with_degree_algo(_, orig: Graph):
    cover_group = []
    graph = orig.copy()
    set_name(graph)

    while not is_empty_graph(graph):
        selected_vertices = select_vertices(graph)
        zero_vertices(graph, selected_vertices)
        cover_group = cover_group + selected_vertices
    return cover_group
