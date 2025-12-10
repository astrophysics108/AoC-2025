from itertools import combinations
from functools import cache
from shapely import *
import numpy as np

# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3""".splitlines()

data = open("day9/input.txt", "r").readlines()

data = [[int(el) for el in line.strip().split(",")] for line in data]

@cache
def straight_line_dist(node1, node2):
    return (abs(node1[0] - node2[0])+1) * (abs(node1[1] - node2[1])+1)

@cache
def are_not_linearly_independent(i,j,k):
    if (k[0] == i[0] and k[1] == j[1]) or (k[0] == j[0] and k[1] == i[1]):
        return True
    else:
        return False
        

# def connections_find():
#     lengths = []
#     for i, j, k in combinations(data, 3):
#         i = tuple(i)
#         j = tuple(j)
#         k = tuple(k)
#         if i != j and i != k  and j != k:
#             for ind in range(3):
#                 if are_not_linearly_independent(tuple(i),tuple(j),tuple(k)):
#                     if (k[0] == i[0] and k[1] == j[1]):
#                         flipped = [j[0], i[1]]
#                         for el in data:
#                             if ((0 >= (el[0] - flipped[0])) == (0 >= (flipped[0] - i[0]))) and ((0 >= (el[1] - flipped[1])) == (0 >= (flipped[1] - j[1]))):
#                                 dist =  max([straight_line_dist(i, j), straight_line_dist(i, k), straight_line_dist(j, k)])
#                                 lengths.append(dist)
#                                 break
#                     if (k[0] == j[0] and k[1] == i[1]):
#                         flipped = [i[0], j[1]]
#                         for el in data:
#                             if ((0 >= (el[0] - flipped[0])) == (0 >= (flipped[0] - j[0]))) and ((0 >= (el[1] - flipped[1])) == (0 >= (flipped[1] - i[1]))):
#                                 dist =  max([straight_line_dist(i, j), straight_line_dist(i, k), straight_line_dist(j, k)])
#                                 lengths.append(dist)
#                                 break
#                 l = [tuple(i), tuple(j), tuple(k)]
#                 i = l[1]
#                 j = l[2]
#                 k = l[0]
                

#     print(max(lengths))

def get_big_shape(data):
    geoms = np.array([(x, y) for x, y in data])
    poly = Polygon(geoms)
    return poly

def connections_find():
    lengths = []
    poly = get_big_shape(data)
    for i, j in combinations(data, 2):
        poly2 = Polygon(np.array([i, [i[0], j[1]], j, [j[0], i[1]]]))
        if i == [9,5] and j == [2,3]:
            ...
        if contains(poly, poly2):
            lengths.append([i,j])
    
    lengths = [straight_line_dist(tuple(el[0]), tuple(el[1])) for el in lengths]
    print(max(lengths))
        



# connections_find()
x = "matilda"

print(x[1000%len(x) - 1])

