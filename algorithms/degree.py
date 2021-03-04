import numpy as np
import random
from igraph import Graph, Vertex
from typing import List
from graph_utils import set_name, split_dataframe_to_averaged_bins
from algorithms.reductions import reduce_graph
import pandas as pd


def is_empty_graph(graph: Graph):
    return len(graph.es) == 0


def select_vertex(graph: Graph):
    v: Vertex
    degree_vector = [v.degree() for v in graph.vs]
    random_vector = np.array([random.random() for i in range(len(degree_vector))])
    fake_degree_vector = random_vector + degree_vector
    max_index = np.argmax(fake_degree_vector)
    max_degree = degree_vector[max_index]

    return graph.vs[max_index]['name'],max_degree


def zero_vertices(graph: Graph, selected_vertices: List[str]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def degree(_: np.ndarray, orig: Graph):

    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    cover_group_degree = []
    removed_counter = 0

    while not is_empty_graph(graph):

        add_to_cover, removed_in_reduce = reduce_graph(graph, do_reduce_1=False, do_reduce_2=False,
                                                       do_reduce_3=False)
        cover_group.extend(add_to_cover)
        removed_counter += removed_in_reduce

        if is_empty_graph(graph):
            break

        selected_vertex, selected_max_degree = select_vertex(graph)
        cover_group_degree.append(selected_max_degree)

        zero_vertices(graph, [selected_vertex])
        cover_group.append(selected_vertex)

    return cover_group, removed_counter,(cover_group_degree,)


def print_g_of_v_extra_metadata(metadata):
    (cover_group_degree,) = metadata
    degree_df = pd.DataFrame({'degree': cover_group_degree})
    averaged_degree_df = split_dataframe_to_averaged_bins(degree_df, 10)
    averaged_degree_df.plot(title='DEGREE algo, degree per iteration')

    print('========= cover_group_degree =========')
    print(cover_group_degree)


degree.extra_metadata = print_g_of_v_extra_metadata
