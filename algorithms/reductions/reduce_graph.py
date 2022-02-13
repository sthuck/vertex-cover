from igraph import Graph, Vertex
from typing import List
from . import remove_parents_of_leaves, remove_vertex_if_contained_neighbors, remove_vertices_with_2_disjoint_neighbors
from dataclasses import dataclass


@dataclass()
class ReductionCounters:
    reduction_1_counter: int = 0
    reduction_2_counter: int = 0
    reduction_3_counter: int = 0


def reduce_graph(graph: Graph, do_reduce_1=True, do_reduce_2=True, do_reduce_3=True, counters: ReductionCounters = None):
    add_to_cover: List[str] = []
    counter_of_removed = 0

    while True:
        reduce_1_worked = reduce_2_worked = reduce_3_worked = False

        if do_reduce_1:
            removed_vertices = remove_parents_of_leaves(graph)
            if len(removed_vertices) > 0:
                reduce_1_worked = True
            add_to_cover.extend(removed_vertices)
            if counters:
                counters.reduction_1_counter += len(removed_vertices)

        if do_reduce_2:
            how_many_removed = remove_vertices_with_2_disjoint_neighbors(graph)
            if how_many_removed > 0:
                reduce_2_worked = True
            counter_of_removed += how_many_removed
            if counters:
                counters.reduction_2_counter += how_many_removed

        if do_reduce_3:
            removed_vertices = remove_vertex_if_contained_neighbors(graph)
            if len(removed_vertices) > 0:
                reduce_3_worked = True
            add_to_cover.extend(removed_vertices)
            if counters:
                counters.reduction_3_counter += len(removed_vertices)

        if not reduce_1_worked and not reduce_2_worked and not reduce_3_worked:
            break

    return add_to_cover, counter_of_removed
