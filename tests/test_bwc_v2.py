from bwc.bwc_min import bwc_min_algo_v2, bwc_min_algo
from graph_utils import random_graph
import time

def test_bwc():
    g = random_graph(1000, 1/1000)
    s1 = time.time()
    _, W = bwc_min_algo(g, 250)
    e1 = time.time()
    s2 = time.time()
    _, W2 = bwc_min_algo_v2(g, 250)
    e2 = time.time()
    print(f' v1 took ${e1-s1}, v2 took ${e2-s2}')
    assert W == W2

