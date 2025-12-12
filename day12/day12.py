presents_list = """0:
#.#
###
#.#

1:
###
###
#..

2:
###
.##
##.

3:
###
.##
..#

4:
###
..#
###

5:
##.
.##""".splitlines()

data = [x.strip() for x in open("day12/input.txt", "r").readlines()]


presents = []
count = 0
for line in presents_list:
    if line.endswith(":"):
        presents.append(count)
        count = 0
    elif "#" in line:
        count += [x for x in line].count("#")

del presents[0]
presents.append(count)


count = 0 
for line in data:
    line = line.split(":")
    x, y = [int(i) for i in line[0].split("x")]
    area = x*y
    no_of_presents = [int(i) for i in line[1].split()]
    area2 = 0
    for i, j in enumerate(no_of_presents):
        area2 += j*(presents[i])
    if area - area2 >= 100:
        count += 1

print(count)
    