from igraph import Graph
from igraph import Vertex
from typing import Tuple, List


def find_parents_of_leaves(graph: Graph):
    all_leaves = [v for v in graph.vs if v.degree() == 1]
    parents = {leaf.neighbors()[0] for leaf in all_leaves}
    return parents


def p0002_graph(graph: Graph):
    graph: Graph = graph or Graph.Erdos_Renyi(1000, 2/1000, None)
    while True:
        parents = find_parents_of_leaves(graph)
        if len(parents) == 0:
            break
        graph.delete_vertices(parents)
    return len(graph.vs)


def is_neighbors(graph: Graph, vertices: Tuple[Vertex, Vertex]):
    v1, v2 = vertices
    return v2 in v1.neighbors()


def find_vertex_with_degree_2_and_disjoint_neighbors(graph: Graph):
    all_vertex_with_degree_2 = [v for v in graph.vs if (v.degree() == 2 and not is_neighbors(graph, v.neighbors()))]
    if len(all_vertex_with_degree_2) > 0:
        return all_vertex_with_degree_2[0]
    else:
        return None


def set_name(graph: Graph):
    for v in graph.vs:
        v['name'] = f'v{v.index}'


def p0003_graph(graph=None):
    graph: Graph = graph or Graph.Erdos_Renyi(1000, 3/1000)
    set_name(graph)

    iteration = 0
    while True:
        parents = find_parents_of_leaves(graph)
        graph.delete_vertices(parents)

        vertex: Vertex = find_vertex_with_degree_2_and_disjoint_neighbors(graph)
        if vertex is None:
            break

        neighbors: List[Vertex] = vertex.neighbors()
        neighbors_of_neighbors = [n['name'] for n in neighbors[0].neighbors() if n.index != vertex.index] + [n['name'] for n in neighbors[1].neighbors() if n.index != vertex.index]
        graph.delete_vertices([vertex] + neighbors)

        graph.add_vertex(name=f'new-iteration{iteration}')
        new_vertex: Vertex = graph.vs.find(name=f'new-iteration{iteration}')

        iteration += 1
        for v in neighbors_of_neighbors:
            graph.add_edge(new_vertex, v)

    components = [c for c in graph.components() if len(c) > 1]
    result = {'how many components': len(components), 'component_length_vector': [len(c) for c in components]}
    return result


if __name__ == '__main__':
    print(p0003_graph())
