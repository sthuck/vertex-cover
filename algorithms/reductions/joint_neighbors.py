from igraph import Graph, Vertex
from typing import List, Union, Tuple


def remove_vertices_with_2_joint_neighbors(graph: Graph):
    how_many_removed = 0

    while True:
        iterator = filter(lambda v: v.degree() == 2, graph.vs)
        how_many_removed_this_iteration = 0

        while True:
            vertex: Vertex = next(iterator, None)

            if vertex is None:
                break

            ## if neighbors are connected
            if is_neighbors(vertex.neighbors()):
                graph.delete_vertices([vertex] + vertex.neighbors())
                how_many_removed_this_iteration += 2
                continue

        how_many_removed += how_many_removed_this_iteration
        if how_many_removed_this_iteration == 0:
            break

    return how_many_removed


def is_neighbors(vertices: Tuple[Vertex, Vertex]):
    v1, v2 = vertices
    return v2 in v1.neighbors()
