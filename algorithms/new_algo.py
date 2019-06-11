from igraph import Graph, Vertex
from typing import List, Tuple


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def compute_t(orig: Graph, vertex: Vertex):
    graph: Graph = orig.copy()
    how_many_neighbors = vertex.degree()
    remove_vertex_and_neighbors(graph, vertex)
    dv_dv_plus_1 = [(v.degree() / (v.degree() + 1)) for v in graph.vs]
    return sum(dv_dv_plus_1) + how_many_neighbors


##
# In return_value[0] returns the vertex found, in  return_value[1] it's neighbors
def select_vertices(graph: Graph) -> Tuple[int, List[int]]:
    t_values = [(v.index, compute_t(graph, v)) for v in graph.vs]
    lowest_t_index = min(t_values, key=lambda item: item[1])[0]
    lowest_t_vertex: Vertex = graph.vs[lowest_t_index]
    return lowest_t_vertex['name'], [v['name'] for v in lowest_t_vertex.neighbors()]


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def remove_vertex_and_neighbors(graph: Graph, v: Vertex):
    graph.delete_vertices([v.index] + [ve.index for ve in v.neighbors()])


def set_name(graph: Graph):
    for v in graph.vs:
        v['name'] = v.index


def new_algo(_, orig: Graph):
    cover_group = []
    graph: Graph = orig.copy()
    set_name(graph)

    while not is_empty_graph(graph):
        selected_vertices = select_vertices(graph)
        zero_vertices(graph, [selected_vertices[0]] + selected_vertices[1])
        cover_group = cover_group + selected_vertices[1]
    return cover_group
