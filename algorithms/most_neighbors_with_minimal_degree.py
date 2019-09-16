from igraph import Graph, Vertex
from typing import List, Tuple
from collections import Counter

from graph_utils import set_name


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def find_maximum(item_list: List[Tuple[int, int]]) -> List[int]:
    max_item = None
    maximum_indices = []
    for index, item in item_list:
        if max_item is None or item > max_item:
            max_item = item
            maximum_indices = [index]
        elif item == max_item:
            maximum_indices.append(index)

    return maximum_indices


def compute_neighbour_degree_frequency(degree_per_vector: List[int], vertex: Vertex):
    degree_vector_for_vertex = [degree_per_vector[neighbour.index] for neighbour in vertex.neighbors()]
    return Counter(degree_vector_for_vertex)


def select_vertices(graph: Graph) -> int:
    degree_per_vector = [v.degree() for v in graph.vs]
    counter_per_vertex = [compute_neighbour_degree_frequency(degree_per_vector, vertex) for vertex in graph.vs]

    degree = 1
    index_of_vertex_with_most_neighbours_of_x_degree = None
    scan_only_indices = [i for i in range(len(graph.vs))]

    while index_of_vertex_with_most_neighbours_of_x_degree is None:
        how_many_neighbours_of_x_degree_per_vertex = \
            [(index, counter_per_vertex[index][degree]) for index in scan_only_indices]

        maximum_indices = find_maximum(how_many_neighbours_of_x_degree_per_vertex)
        if len(maximum_indices) > 1:
            scan_only_indices = maximum_indices
            degree = degree + 1

            if degree > len(graph.vs):  # if degree > vertex number, just take the first one
                index_of_vertex_with_most_neighbours_of_x_degree = maximum_indices[0]
        else:
            index_of_vertex_with_most_neighbours_of_x_degree = maximum_indices[0]

    return graph.vs[index_of_vertex_with_most_neighbours_of_x_degree]['name']


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def remove_vertex_and_neighbors(graph: Graph, v: Vertex):
    graph.delete_vertices([v.index] + [ve.index for ve in v.neighbors()])


def most_neighbors_with_minimal_degree_algo(_, orig: Graph):
    cover_group = []
    graph: Graph = orig.copy()
    set_name(graph)

    while not is_empty_graph(graph):
        selected_vertex = select_vertices(graph)
        zero_vertices(graph, [selected_vertex])
        cover_group = cover_group + [selected_vertex]
    return cover_group
