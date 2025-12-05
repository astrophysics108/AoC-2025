# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.""".splitlines()

data = open("day4/day4.txt", "r").readlines()
data = [[x for x in el.strip()] for el in data]
transformations = [(1,0), (-1, -1), (1,1), (-1, 0), (0, -1), (0, 1), (1, -1), (-1, 1)]


out = 0

num_removed_prev = None

while num_removed_prev != 0:
    num_removed_prev = 0
    for j, line in enumerate(data):
        for i, el in enumerate(line):
            num_rolls = 0
            if el == "@":
                for t in transformations:
                        newind1 = j+t[0]
                        newind2 = i+t[1]
                        if 0 <= newind1 < len(data) and 0 <= newind2 < len(line) and data[newind1][newind2] == "@":
                            num_rolls += 1
                            
                if num_rolls < 4:
                    out += 1
                    line[i] = "x"
                    num_removed_prev += 1
                #print(line, i)

# [print(line) for line in data]
print(out)