import numpy as np
import random
from igraph import Graph, Vertex
from typing import List
from graph_utils import set_name
from algorithms.reductions import reduce_graph


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0




def select_vertex(graph: Graph):
    v: Vertex
    degree_vector = [v.degree() for v in graph.vs]
    random_vector = np.array([random.random() for i in range(len(degree_vector))])
    fake_degree_vector = random_vector + degree_vector
    max_index = np.argmax(fake_degree_vector)
    return graph.vs[max_index]['name']


def zero_vertices(graph: Graph, selected_vertices: List[str]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def degree(_: np.ndarray, orig: Graph):

    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    removed_counter = 0

    while not is_empty_graph(graph):

        add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=True)
        cover_group.extend(add_to_cover)
        removed_counter += removed_in_reduce

        if is_empty_graph(graph):
            break

        selected_vertex = select_vertex(graph)
        zero_vertices(graph, [selected_vertex])
        cover_group.append(selected_vertex)

    return cover_group, removed_counter
