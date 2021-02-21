import numpy as np
import random
import pandas as pd
from igraph import Graph, Vertex
from typing import List
from graph_utils import set_name
from g_of_v.g_of_v import compute_g_of_v
from g_of_v.g_of_v import compute_g_of_v_for_testing
import math

def compute_g_of_v_for_testing_orig(graph: Graph):
    v: Vertex
    g_of_v_vector_plus_degree = [compute_g_of_v_for_testing(v) if v.degree() > 0 else (0, 0, 0) for v in graph.vs]

    return g_of_v_vector_plus_degree

def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def select_vertex(graph: Graph):
    v: Vertex
    g_of_v_vector = [compute_g_of_v(v) if v.degree() > 0 else -math.inf for v in graph.vs]
    max_index = np.argmax(g_of_v_vector)
    g_of_v_value = g_of_v_vector[max_index]
    degree = graph.vs[max_index].degree()

    return graph.vs[max_index]['name'], g_of_v_value, degree


def zero_vertices(graph: Graph, selected_vertices: List[str]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def g_of_v_algo(_: np.ndarray, orig: Graph):

    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    cover_group_degree = []
    cover_group_g_of_v = []
    removed_counter = 0

    while not is_empty_graph(graph):

        if is_empty_graph(graph):
            break

        selected_vertex, g_of_v_value, degree = select_vertex(graph)
        cover_group_degree.append(degree)
        cover_group_g_of_v.append(g_of_v_value)

        zero_vertices(graph, [selected_vertex])
        cover_group.append(selected_vertex)

    return cover_group, removed_counter, (cover_group_degree, cover_group_g_of_v)


def print_g_of_v_extra_metadata(metadata):
    (cover_group_degree, cover_group_g_of_v) = metadata
    degree_df = pd.DataFrame({'degree': cover_group_degree})
    degree_df.plot(title='g_of_v algo, degree per iteration', kind='bar')
    g_of_v_df = pd.DataFrame({'g of v': cover_group_g_of_v})
    g_of_v_df.plot(title='g_of_v algo, g_of_v_value per iteration')

    print('========= cover_group_degree =========')
    print(cover_group_degree)
    print('========= cover_group_g_of_v =========')
    print(cover_group_g_of_v)



g_of_v_algo.extra_metadata = print_g_of_v_extra_metadata
