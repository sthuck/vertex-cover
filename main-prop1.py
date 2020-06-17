from algorithms import shaked_algo_impl
from graph_utils import graph_to_numpy, read_dimacs, graph_stats, dv_divide_dv_plus_1
from igraph import Graph
from prop1.graph_data import formula_prop_1
import numpy as np

filename = "p_hat1000-3.clq"

def main():
    iterations = 1000

    try:
        (orig_graph, orig_np_graph) = read_dimacs("./example-graph/" + filename, reverse=True)
    except:
        print(f'=====FAIL ======')
        print(f'failed reading graph {filename}')
        exit(-1)

    stats = graph_stats(orig_np_graph)
    stats.update({'Graph name': filename, 'Edges Num': len(orig_graph.es), 'Vertex Num': len(orig_graph.vs)})

    print('graph:', filename,  stats)

    results = []
    for i in range(iterations):
        np_graph = orig_np_graph.copy()
        cover_group = shaked_algo_impl.shaked_algo_impl(np_graph, randomize=True)
        cover_group_size = len(cover_group)
        print(f'iteration {i}: {cover_group_size}')
        results.append(cover_group_size)
    print('=========')
    avg = np.array(results).mean()
    print(f'average: {avg}')
    variance = np.array(results).var()
    print(f'variance: {variance}')
    dv_dv1 = dv_divide_dv_plus_1(orig_graph)
    print(f'1A: {dv_dv1}')
    prop1_result = formula_prop_1(orig_graph)
    print(f'1B: {prop1_result}')



if __name__ == '__main__':
    main()