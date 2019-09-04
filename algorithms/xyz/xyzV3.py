import numpy as np
import scipy.sparse as sp
import scipy
from .xyz_utils import all_vertex_degree, is_empty_graph as is_empty_graph_sparse
from .xyz_common_code import get_x_vector, get_y_vector, get_z_vector
from igraph import Graph, Vertex
from typing import List, Union, Tuple


def xyz_select_vertex(graph: Graph) -> Union[int, None]:
    sparse = build_sparse(graph)

    if is_empty_graph_sparse(sparse):
        return None

    vertex_degree_vector = all_vertex_degree(sparse)

    x_vector = get_x_vector(vertex_degree_vector)
    y_vector = get_y_vector(sparse, x_vector)
    z_vector = get_z_vector(sparse, vertex_degree_vector)

    diff_vector = z_vector - y_vector
    return diff_vector.argmin()


def get_all_leaves(graph: sp.lil_matrix):
    degree_vertex = all_vertex_degree(graph)
    leaves = np.where(degree_vertex == 1)[0]
    return leaves


def get_parent_of_leaf(graph: sp.lil_matrix, leaf_index: int):
    # graph[leaf_index] returns matrix of one column, so np.nonzero also returns matrix
    possible_parent = np.nonzero(graph[leaf_index])[1]

    return possible_parent[0] if len(possible_parent) == 1 else None


def zero_vertices(graph: Graph, selected_vertices: List[int]):
    selected_set = graph.vs.select(name_in=selected_vertices)
    graph.delete_vertices(selected_set)


def zero_vertices_by_index(graph: Graph, vertex: Union[int, List[int]]):
    graph.delete_vertices(vertex)


def set_name(graph: Graph):
    for v in graph.vs:
        v['name'] = f'v{v.index}'


def build_sparse(graph: Graph):
    return scipy.sparse.csr_matrix(graph.get_adjacency().data)


def find_parents_of_leaves(graph: Graph):
    all_leaves = [v for v in graph.vs if v.degree() == 1]
    parents = {leaf.neighbors()[0] for leaf in all_leaves}
    return parents


def remove_parents_of_leaves(graph: Graph) -> List[int]:
    add_to_cover = []
    while True:
        parents = find_parents_of_leaves(graph)
        if len(parents) == 0:
            break
        add_to_cover.extend([v['name'] for v in parents])
        graph.delete_vertices(parents)

    return add_to_cover


def find_vertex_with_degree_2_and_disjoint_neighbors(graph: Graph):
    all_vertex_with_degree_2 = [v for v in graph.vs if (v.degree() == 2 and not is_neighbors(v.neighbors()))]
    if len(all_vertex_with_degree_2) > 0:
        return all_vertex_with_degree_2[0]
    else:
        return None


def is_neighbors(vertices: Tuple[Vertex, Vertex]):
    v1, v2 = vertices
    return v2 in v1.neighbors()


def remove_vertices_with_2_disjoint_neighbors(graph: Graph):

    counter = 0
    while True:
        vertex: Vertex = find_vertex_with_degree_2_and_disjoint_neighbors(graph)
        if vertex is None:
            break

        neighbors: List[Vertex] = vertex.neighbors()
        neighbors_of_neighbors = [n['name'] for n in neighbors[0].neighbors() if n.index != vertex.index] + \
                                 [n['name'] for n in neighbors[1].neighbors() if n.index != vertex.index]

        graph.delete_vertices([vertex] + neighbors)

        graph.add_vertex(name=f'new-iteration{remove_vertices_with_2_disjoint_neighbors.counter}')
        new_vertex: Vertex = graph.vs.find(name=f'new-iteration{remove_vertices_with_2_disjoint_neighbors.counter}')

        remove_vertices_with_2_disjoint_neighbors.counter += 1
        for v in neighbors_of_neighbors:
            graph.add_edge(new_vertex, v)
        counter = counter + 1
    return counter


remove_vertices_with_2_disjoint_neighbors.counter = 0


def remove_vertex_if_contained_neighbors(graph: Graph):
    to_remove_set = set()
    v: Vertex
    for v in graph.vs:
        u: Vertex
        for u in v.neighbors():
            if set(v.neighbors()).issuperset(set(u.neighbors())):
                to_remove_set.add(v)

    add_to_cover_list = [v['name'] for v in to_remove_set]

    zero_vertices_by_index(graph, [v.index for v in to_remove_set])
    return add_to_cover_list


def xyz_v3_algo(_, orig: Graph):
    graph: Graph = orig.copy()
    set_name(graph)

    cover_group = []
    removed_vertices_with_2_disjoint_neighbors_counter = 0

    while True:

        # Phase 1
        add_to_cover = remove_parents_of_leaves(graph)
        cover_group += add_to_cover

        # Phase 2
        how_many_removed = remove_vertices_with_2_disjoint_neighbors(graph)
        removed_vertices_with_2_disjoint_neighbors_counter += how_many_removed

        # Phase 3
        add_to_cover = remove_vertex_if_contained_neighbors(graph)
        cover_group += add_to_cover

        # xyz
        selected_vertex_index = xyz_select_vertex(graph)
        if selected_vertex_index is None:
            break
        cover_group.append(graph.vs[selected_vertex_index]['name'])
        zero_vertices_by_index(graph, selected_vertex_index)
    return list(cover_group), removed_vertices_with_2_disjoint_neighbors_counter
