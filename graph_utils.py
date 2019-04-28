from igraph import Graph, ADJ_UNDIRECTED, Vertex
from igraph.drawing import plot
from typing import List
import numpy as np
import re
import sys
import csv


# graph.write('output.graphml', format='graphml')
# layout = graph.layout_grid(width=10, height=10, dim=3)
# graph.write_svg('./out.svg', labels=[str(i) for i in range(n)])


def random_graph(n, p):
    graph: Graph = Graph.Erdos_Renyi(n, p)
    return graph


def random_graph_by_edges(n, e):
    graph: Graph = Graph.Erdos_Renyi(n, m=e)
    return graph


def write_to_graphml(graph: Graph, vertices):
    graph.vs["name"] = [str(i) for i in range(graph.vcount())]
    graph.vs["color"] = [
        'deepskyblue' if i in vertices else 'indianred' for i in range(graph.vcount())]
    graph.write('output.graphml', format='graphml')


def write_to_file(file_name: str, graph: Graph, vertices):
    options = {
        'labels': [str(i) for i in range(graph.vcount())],
        'colors': ['deepskyblue' if i in vertices else 'indianred' for i in range(graph.vcount())],
        'layout': graph.layout_auto()
    }
    graph.write_svg(file_name, height=800, width=800, **options)


def graph_to_numpy(graph: Graph):
    n = graph.vcount()
    a = np.zeros((n, n), dtype=np.byte)
    if len(graph.get_edgelist()) == 0:
        print('got empty graph, no edges')
        sys.exit(-1)
    rows, cols = zip(*graph.get_edgelist())
    a[rows, cols] = 1
    a[cols, rows] = 1
    # a = np.array(graph.get_adjacency().data) --BENCHMARK
    return a


def read_dimacs(filename: str, reverse=False):
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
            if re.search(r'^e (\d*) (\d*).*', line):
                match = re.search(r'^e (\d*) (\d*).*', line)
                source = int(match.group(1))  # dimacs are not 0-index
                dest = int(match.group(2))
                matrix[source - 1, dest - 1] = 1
                matrix[dest - 1, source - 1] = 1
            elif re.search('^c .*', line):
                pass
            elif re.search(r'^p edge (\d*) .*', line):
                match = re.search(r'^p edge (\d*) .*', line)
                vertices_num = int(match.group(1))
                matrix = np.zeros((vertices_num, vertices_num), dtype=np.byte)

    if reverse:
        reverse_matrix = np.ones_like(matrix) - matrix

        for i in range(len(reverse_matrix)):
            reverse_matrix[i, i] = 0

        matrix = reverse_matrix

    graph: Graph = Graph.Adjacency(matrix.tolist(), mode=ADJ_UNDIRECTED)
    return graph, matrix


def graph_stats(graph: np.ndarray):
    degree_vertex: np.ndarray = graph.sum(axis=0)
    min_degree = degree_vertex.min()
    max_degree = degree_vertex.max()
    average_degree = degree_vertex.sum() / len(degree_vertex)
    how_many_leaves = np.count_nonzero(degree_vertex == 1)
    return {'Minimum Degree': min_degree, 'Max Degree': max_degree,
            'Average Degree': average_degree, 'Num of leaves': how_many_leaves}


def write_csv_stats(stats: List[dict]):
    with open('stats.csv', 'w', newline='') as csvfile:
        fieldnames = stats[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(stats)


def check_if_legal_vertex_cover(graph: np.ndarray, vertex_cover: List[int]):
    not_in_cover = [v for v in range(len(graph)) if v not in vertex_cover]
    for v in not_in_cover:
        for v2 in not_in_cover:
            if graph[v][v2] == 1:
                return False
    return True


def all_neighbors_rank_1(v: Vertex):
    return any([n.degree() == 1 for n in v.neighbors()])


def count_parents_of_leaves(graph: Graph):
    parents_degree_1 = [v for v in graph.vs if v.degree() == 1 and all_neighbors_rank_1(v)]
    parents = [v for v in graph.vs if v.degree() > 1 and all_neighbors_rank_1(v)]
    assert len(parents_degree_1) % 2 == 0, "Number of parents with degree 1 must be even!"
    return len(parents) + len(parents_degree_1) / 2
