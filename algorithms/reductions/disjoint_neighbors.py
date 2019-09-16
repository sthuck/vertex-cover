from igraph import Graph, Vertex
from typing import List, Union, Tuple

global_counter_for_vertex_name = 0


def remove_vertices_with_2_disjoint_neighbors(graph: Graph):
    global global_counter_for_vertex_name
    how_many_removed = 0

    while True:
        vertex: Vertex = next(filter(lambda v: v.degree() == 2, graph.vs), None)

        if vertex is None:
            break

        # if neighbors are connected
        if is_neighbors(vertex.neighbors()):
            graph.delete_vertices(vertex.neighbors())
            graph.delete_vertices(vertex)
            how_many_removed += 2
            continue

        # if neighbors are not connected
        neighbors: List[Vertex] = vertex.neighbors()
        neighbors_of_neighbors = {n['name'] for n in neighbors[0].neighbors() if n.index != vertex.index}.union(
                                 {n['name'] for n in neighbors[1].neighbors() if n.index != vertex.index})

        graph.delete_vertices([vertex] + neighbors)

        graph.add_vertex(name=f'new-iteration{global_counter_for_vertex_name}')
        new_vertex: Vertex = graph.vs.find(name=f'new-iteration{global_counter_for_vertex_name}')

        global_counter_for_vertex_name += 1

        for n in neighbors_of_neighbors:
            graph.add_edge(new_vertex, n)
        how_many_removed = how_many_removed + 1

    return how_many_removed


def is_neighbors(vertices: Tuple[Vertex, Vertex]):
    v1, v2 = vertices
    return v2 in v1.neighbors()
