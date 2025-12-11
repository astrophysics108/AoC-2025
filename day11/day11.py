import networkx as nx
from functools import cache
# data = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out""".splitlines()

data = [x.strip() for x in open("day11/input.txt", "r").readlines()]
# circuit = nx.DiGraph()
# for line in data:
#     line = line.split(":")
#     conn = line[1].split()
#     print(line)
#     circuit.add_edges_from([(line[0], x) for x in conn])

data = {el.split(":")[0]:[a for a in el.split(":")[1].split()] for el in data}
# paths = list(nx.all_simple_paths(circuit, "svr", "out"))
# out = 0
# for path in paths:
#     print(path)
#     if "fft" in path and "dac" in path:
#         out += 1
# print(out)


@cache
def dfs_through_paths(node_name, fft, dac, increment):
    if node_name == "out" and fft and dac:
        increment += 1
        return increment
    elif node_name == "out":
        return increment
    else:
        if node_name == "fft":
            fft = True
        elif node_name == "dac":
            dac = True
        total = 0
        for node in data[node_name]:
            total += dfs_through_paths(node, fft, dac, increment)
        return total

out = dfs_through_paths("svr", False, False, 0)
print(out)
