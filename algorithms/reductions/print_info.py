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
    return {'How many components': len(components), 'Component length vector': [len(c) for c in components]}


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


def print_theortical_number_of_leaves(n, c):
    leaves = n * c * (math.pow(math.e, -c))
    parents_of_leaves = n * (1 - math.pow(math.e, (-c * math.pow(math.e, -c))))
    vertices_with_degree = n * math.pow(math.e, -c)

    print(f'Therotical number of leaves: {leaves}')
    print(f'Therotical number of parents of leaves: {parents_of_leaves}')
    print(f'Therotical number of vertices with degree 0: {vertices_with_degree}')
