from igraph import Graph, Vertex
from typing import List, Union, Tuple


def remove_vertices_with_2_disjoint_neighbors(graph: Graph):

    counter = 0
    while True:
        vertex: Vertex = find_vertex_with_degree_2_and_disjoint_neighbors(graph)
        if vertex is None:
            break

        neighbors: List[Vertex] = vertex.neighbors()
        neighbors_of_neighbors = {n['name'] for n in neighbors[0].neighbors() if n.index != vertex.index}.union(
                                 {n['name'] for n in neighbors[1].neighbors() if n.index != vertex.index})

        graph.delete_vertices([vertex] + neighbors)

        graph.add_vertex(name=f'new-iteration{remove_vertices_with_2_disjoint_neighbors.counter}')
        new_vertex: Vertex = graph.vs.find(name=f'new-iteration{remove_vertices_with_2_disjoint_neighbors.counter}')

        remove_vertices_with_2_disjoint_neighbors.counter += 1
        for v in neighbors_of_neighbors:
            graph.add_edge(new_vertex, v)
        counter = counter + 1
    return counter


remove_vertices_with_2_disjoint_neighbors.counter = 0


def find_vertex_with_degree_2_and_disjoint_neighbors(graph: Graph):
    all_vertex_with_degree_2 = [v for v in graph.vs if (v.degree() == 2 and not is_neighbors(v.neighbors()))]
    if len(all_vertex_with_degree_2) > 0:
        return all_vertex_with_degree_2[0]
    else:
        return None


def is_neighbors(vertices: Tuple[Vertex, Vertex]):
    v1, v2 = vertices
    return v2 in v1.neighbors()
