import numpy as np
import random
import pandas as pd
from igraph import Graph, Vertex
from typing import List
from graph_utils import set_name
from g_of_v.g_of_v import compute_g_of_v , compute_g_of_v_bwc
from g_of_v.g_of_v import compute_g_of_v_for_testing
import math
from graph_utils import allmax_index, split_dataframe_to_averaged_bins


def compute_g_of_v_for_testing_orig(graph: Graph):
    v: Vertex
    g_of_v_vector_plus_degree = [compute_g_of_v_for_testing(v) if v.degree() > 0 else (0, 0, 0) for v in graph.vs]

    return g_of_v_vector_plus_degree


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def select_vertex(graph: Graph, iteration: int):
    v: Vertex
    g_of_v_vector = [compute_g_of_v(v) if v.degree() > 0 else -math.inf for v in graph.vs]

    max_indices = allmax_index(g_of_v_vector)
    print(f'g_of_v iteration: {iteration}, number of max g {len(max_indices)}, value: {g_of_v_vector[max_indices[0]]}, indices: {",".join([str(s) for s in max_indices])}')
    max_index = max_indices[random.randint(0, len(max_indices) - 1)]

    g_of_v_value = g_of_v_vector[max_index]
    degree = graph.vs[max_index].degree()

    return graph.vs[max_index]['name'], g_of_v_value, degree

def select_vertex_bwc(graph: Graph, iteration: int):
    v: Vertex
    g_of_v_vector = [compute_g_of_v_bwc(v) if v.degree() > 0 else -math.inf for v in graph.vs]

    max_indices = allmax_index(g_of_v_vector)
    print(f'g_of_v iteration: {iteration}, number of max g {len(max_indices)}, value: {g_of_v_vector[max_indices[0]]}, indices: {",".join([str(s) for s in max_indices])}')
    max_index = max_indices[random.randint(0, len(max_indices) - 1)]

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
    iteration = 0
    while not is_empty_graph(graph):
        iteration += 1

        if is_empty_graph(graph):
            break

        selected_vertex, g_of_v_value, degree = select_vertex(graph, iteration)
        cover_group_degree.append(degree)
        cover_group_g_of_v.append(g_of_v_value)

        zero_vertices(graph, [selected_vertex])
        cover_group.append(selected_vertex)

    return cover_group, removed_counter, (cover_group_degree, cover_group_g_of_v)

def g_of_v_algo_bwc(_: np.ndarray, orig: Graph):

    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    cover_group_degree = []
    cover_group_g_of_v = []
    removed_counter = 0
    iteration = 0
    while not is_empty_graph(graph):
        iteration += 1

        if is_empty_graph(graph):
            break

        selected_vertex, g_of_v_value, degree = select_vertex_bwc(graph, iteration)
        cover_group_degree.append(degree)
        cover_group_g_of_v.append(g_of_v_value)

        zero_vertices(graph, [selected_vertex])
        cover_group.append(selected_vertex)

    return cover_group, removed_counter, (cover_group_degree, cover_group_g_of_v)


def print_g_of_v_extra_metadata(metadata):
    (cover_group_degree, cover_group_g_of_v) = metadata
    degree_df = pd.DataFrame({'degree': cover_group_degree})
    averaged_degree_df = split_dataframe_to_averaged_bins(degree_df, 10)
    averaged_degree_df.plot(title='g_of_v algo, degree per iteration')

    g_of_v_df = pd.DataFrame({'g of v': cover_group_g_of_v})
    averaged_g_of_v_df = split_dataframe_to_averaged_bins(g_of_v_df, 10)
    averaged_g_of_v_df.plot(title='g_of_v algo, g_of_v_value per iteration')

    print('========= cover_group_degree =========')
    print(cover_group_degree)
    print('========= cover_group_g_of_v =========')
    print(cover_group_g_of_v)


g_of_v_algo.extra_metadata = print_g_of_v_extra_metadata
