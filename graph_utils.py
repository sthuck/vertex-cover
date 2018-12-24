from igraph import Graph
from igraph.drawing import plot
import numpy as np
import re

# graph.write('output.graphml', format='graphml')
# layout = graph.layout_grid(width=10, height=10, dim=3)
# graph.write_svg('./out.svg', labels=[str(i) for i in range(n)])


def random_graph(n, p):
    graph: Graph = Graph.Erdos_Renyi(n, p)
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
    rows, cols = zip(*graph.get_edgelist())
    a[rows, cols] = 1
    a[cols, rows] = 1
    # a = np.array(graph.get_adjacency().data) --BENCHMARK
    return a


def read_dimacs(filename: str):
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
            if re.search(r'^e (\d*) (\d*) .*', line):
                match = re.search(r'^e (\d*) (\d*) .*', line)
                source = int(match(1))
                dest = int(match(2))
                matrix[source, dest] = 1
                matrix[dest, source] = 1
            elif re.search('^c .*', line):
                pass
            elif re.search(r'^p edge (\d*) .*', line):
                match = re.search(r'^p edge (\d*) .*', line)
                vertices_num = int(match.group(1))
                matrix = np.zeros((vertices_num, vertices_num))

    graph = Graph.Adjacency(matrix.tolist())
    return (graph, matrix)
