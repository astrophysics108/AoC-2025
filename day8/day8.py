import networkx as nx
from itertools import combinations

# data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689""".splitlines()

data = [el.strip() for el in open("day8/input.txt").readlines()]

nums = {el.strip():[int(x) for x in el.strip().split(",")] for el in data}
data = [el.strip() for el in data]

junctions = nx.Graph()

for n in data:
    junctions.add_node(n)

def straight_line_dist(node1, node2):
    node1 = nums[node1]
    node2 = nums[node2]
    squares = 0
    for i in range(3):
        squares += (node1[i] - node2[i])**2
    
    return squares**0.5 


def find_connections():
    global junctions, data
    lengths = {}
    for i, j in combinations(data, 2):
        if i != j:
            dist =  straight_line_dist(i, j)
            lengths[dist] = [i, j]
    
    while not nx.is_connected(junctions):
        closest = lengths[min(lengths.keys())]
        del lengths[min(lengths.keys())]
        junctions.add_edge(closest[0], closest[1])
    
    nodes1 = nums[closest[0]]
    nodes2 = nums[closest[1]]
    print(nodes1[0]*nodes2[0])


find_connections()
# largest_cc = sorted(nx.connected_components(junctions), key=len)
# out = len(largest_cc[-1])*len(largest_cc[-2])*len(largest_cc[-3])
# print(out)


        









