from graph_utils import *
import time
from algorithms.vsa import vsa
from algorithms.degree import degree
from algorithms.shaked_algo_impl import shaked_algo_impl
from algorithms.xyz import xyz_v2_algo, xyz_v3_algo
from algorithms.neighbors_algo import neighbors_algo
from algorithms.xyz_neighbors_combined import xyz_neighbors_combined_algo
from algorithms.most_neighbors_with_minimal_degree import most_neighbors_with_minimal_degree_algo
from algorithms.novac1 import novac1_algo


def simple_becnh(fn):
    start = time.time()
    fn()
    end = time.time()
    print('total time:', end - start)


def main():
    # Definitions
    filenames = [
        # "brock200_1.clq",
        # "brock200_2.clq",
        # "brock200_3.clq",
        # "brock200_4.clq",
        # "brock400_1.clq",
        # "brock400_2.clq",
        # "brock400_3.clq",
        # "brock400_4.clq",
        # "brock800_1.clq",
        # "brock800_2.clq",
        # "brock800_3.clq",
        # "brock800_4.clq",
        # "c-fat200-1.clq",
        # "c-fat200-2.clq",
        # "c-fat200-5.clq",
        # "c-fat500-1.clq",
        # "c-fat500-10.clq",
        # "c-fat500-2.clq",
        # "c-fat500-5.clq",
        # "C1000.9.clq",
        # "C125.9.clq",
        # "C2000.5.clq",
        # "C2000.9.clq",
        # "C250.9.clq",
        # "C4000.5.clq",
        # "C500.9.clq",
        #  "DSJC1000_5.clq",
        # "DSJC500_5.clq",
        # "gen200_p0.9_44.clq",
        # "gen200_p0.9_55.clq",
        # "gen400_p0.9_55.clq",
        # "gen400_p0.9_65.clq",
        # "gen400_p0.9_75.clq",
        # "hamming10-2.clq",
        # "hamming10-4.clq",
        # "hamming6-2.clq",
        # "hamming6-4.clq",
        # "hamming8-2.clq",
        # "hamming8-4.clq",
        # "johnson16-2-4.clq",
        # "johnson32-2-4.clq",
        # "johnson8-2-4.clq",
        # "johnson8-4-4.clq",
        # "keller4.clq",
        # "keller5.clq",
        # "keller6.clq",
        # "MANN_a27.clq",
        # "MANN_a45.clq",
        # "MANN_a81.clq",
        # "MANN_a9.clq",
        #  "p_hat1000-1.clq",
        # "p_hat1000-2.clq",
        # "p_hat1000-3.clq",
        # "p_hat1500-1.clq",
        # "p_hat1500-2.clq",
        # "p_hat1500-3.clq",
        # "p_hat300-1.clq",
        # "p_hat300-2.clq",
        # "p_hat300-3.clq",
        # "p_hat500-1.clq",
        # "p_hat500-2.clq",
        # "p_hat500-3.clq",
        # "p_hat700-1.clq",
        # "p_hat700-2.clq",
        # "p_hat700-3.clq",
        # "san1000.clq",
        # "san200_0.7_1.clq",
        # "san200_0.7_2.clq",
        # "san200_0.9_1.clq",
        # "san200_0.9_2.clq",
        # "san200_0.9_3.clq",
        # "san400_0.5_1.clq",
        # "san400_0.7_1.clq",
        # "san400_0.7_2.clq",
        # "san400_0.7_3.clq",
        # "san400_0.9_1.clq",
        # "sanr200_0.7.clq",
        # "sanr200_0.9.clq",
        "sanr400_0.5.clq",
        # "sanr400_0.7.clq",
        # "frb/frb100-40.mis",
        # "frb/frb30-15-1.mis",
        # "frb/frb30-15-2.mis",
        # "frb/frb30-15-3.mis",
        # "frb/frb30-15-4.mis",
        # "frb/frb30-15-5.mis",
        # "frb/frb35-17-1.mis",
        # "frb/frb35-17-2.mis",
        # "frb/frb35-17-3.mis",
        # "frb/frb35-17-4.mis",
        # "frb/frb35-17-5.mis",
        # "frb/frb40-19-1.mis",
        # "frb/frb40-19-2.mis",
        # "frb/frb40-19-3.mis",
        # "frb/frb40-19-4.mis",
        # "frb/frb40-19-5.mis",
        # "frb/frb45-21-1.mis",
        # "frb/frb45-21-2.mis",
        # "frb/frb45-21-3.mis",
        # "frb/frb45-21-4.mis",
        # "frb/frb45-21-5.mis",
        # "frb/frb50-23-1.mis",
        # "frb/frb50-23-2.mis",
        # "frb/frb50-23-3.mis",
        # "frb/frb50-23-4.mis",
        # "frb/frb50-23-5.mis",
        # "frb/frb53-24-1.mis",
        # "frb/frb53-24-2.mis",
        # "frb/frb53-24-3.mis",
        # "frb/frb53-24-4.mis",
        # "frb/frb53-24-5.mis",
        # "frb/frb56-25-1.mis",
        # "frb/frb56-25-2.mis",
        # "frb/frb56-25-3.mis",
        # "frb/frb56-25-4.mis",
        # "frb/frb56-25-5.mis",
        # "frb/frb59-26-1.mis",
        # "frb/frb59-26-2.mis",
        # "frb/frb59-26-3.mis",
        # "frb/frb59-26-4.mis",
        # "frb/frb59-26-5.mis"

    ]
    # algorithms = [vsa, vsa_by_min, C, shaked_algo, shaked_algo_impl, xyz_algo, xyz_v2_algo, xyz_larger_diff_algo, first_vertex_with_degree_algo, neighbors_algo]
    algorithms = [novac1_algo, xyz_v3_algo, degree]

    # End Definitions

    all_graph_stats = []

    for file in filenames:
        (graph, np_graph) = read_dimacs("./example-graph/" + file, reverse=True)

        stats = graph_stats(np_graph)
        stats.update({'Graph name': file, 'Edges Num': len(graph.es), 'Vertex Num': len(graph.vs)})
        stats.update({'parents of leaves': count_parents_of_leaves(graph)})

        print('graph:', file, '   number of edges:', len(graph.es))
        np_graph = graph_to_numpy(graph)
        for algorithm in algorithms:
            np_graph_copy = np.copy(np_graph)
            result = algorithm(np_graph_copy, graph)
            if any(name == algorithm.__name__ for name in ['xyz_v3_algo', 'xyz_weak_algo']):
                print(algorithm.__name__, '::', len(result[0]) + result[1])
                stats.update({algorithm.__name__: len(result[0]) + result[1]})

            elif algorithm.__name__ == 'shaked_algo':
                print(algorithm.__name__, '::', result)
                stats.update({'Sigma D(Vi)/D(Vi)+1': result})

            else:
                print(algorithm.__name__, '::', len(result))
                stats.update({algorithm.__name__: len(result)})

        all_graph_stats.append(stats)
        print("#####\n\n")

    write_csv_stats(all_graph_stats)


if __name__ == '__main__':
    simple_becnh(main)
