from igraph import Graph, Vertex
import pprint
import math


def info_leaves(graph: Graph):
    v: Vertex
    all_leaves = [v for v in graph.vs if v.degree() == 1]
    parents_of_leaves = set()
    for leaf in all_leaves:
        if leaf not in parents_of_leaves:
            parents_of_leaves.add(leaf.neighbors()[0])
    return {'Number of leaves': len(all_leaves), 'Number of parents of leaves': len(parents_of_leaves)}


def info_zero_degree(graph: Graph):
    v: Vertex
    not_connected = [v for v in graph.vs if v.degree() == 0]
    return {'Number of vertices with degree 0': len(not_connected)}


def info_connected_components(graph: Graph):
    components = [c for c in graph.components() if len(c) > 1]
    components_with_size_2 = [c for c in graph.components() if len(c) == 2]
    return {'How many components': len(components), 'Component length vector': ', '.join([str(len(c)) for c in components]),
            'Components with size 2': len(components_with_size_2)}


def print_graph_info(graph: Graph, leaves=False, zero_degree=False, connected_components=False, label=None):
    if leaves or zero_degree or connected_components:
        result = dict()
        if leaves:
            result.update(info_leaves(graph))
        if zero_degree:
            result.update(info_zero_degree(graph))
        if connected_components:
            result.update(info_connected_components(graph))

        if label:
            pprint.pprint(f'==== {label} ====')
        pprint.pprint(result)
        print()


def print_theoretical_number_of_leaves(n, c):
    leaves = n * c * (math.pow(math.e, -c))
    parents_of_leaves = n * (1 - math.pow(math.e, (-c * math.pow(math.e, -c))))
    vertices_with_degree = n * math.pow(math.e, -c)
    components_with_size_2 = n * c * math.pow(math.e, -2 * c) / 2
    vertices_with_degree_2_and_non_connected_neighbors = n * math.pow(c, 2) * math.pow(math.e, -3 * c) / 2

    print(f'Theoretical number of leaves: {leaves}')
    print(f'Theoretical number of parents of leaves: {parents_of_leaves}')
    print(f'Theoretical number of vertices with degree 0: {vertices_with_degree}')
    print(f'Theoretical number of components with size 2: {components_with_size_2}')
    print(f'Theoretical number of vertices with degree 2 and non connected neighbors: '
          f'{vertices_with_degree_2_and_non_connected_neighbors}')
