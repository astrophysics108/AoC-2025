data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()

data = [el.strip() for el in open("day5/day5.txt", "r").readlines()]

ranges = []
ranges2 = {}
ranges3 = []
ranges4 = []
ids = []
for el in data:
    if "-" in el:
        el = [int(x) for x in el.split("-")]
        ranges.append(range(el[0], el[1]+1))
        ranges3.append(el[0])
        if el[0] not in ranges2.keys():
            ranges2[el[0]] = el[1] + 1
        else:
            ranges2[el[0]] = [ranges2[el[0]]] if type(ranges2[el[0]]) == int else ranges2[el[0]]
            ranges2[el[0]].append(el[1] + 1)
            ranges2[el[0]].sort()
    else:
        try:
            ids.append(int(el))
        except:
            pass

# print(ranges, ids)

def p1():
    fresh = 0
    for id in ids:
        for el in ranges:
            if id in el:
                fresh += 1
                break

    print(fresh)

total = 0

prev_max = 0
prev_min = 0
ranges3 = sorted(ranges3)
nums = set()

for min_num in ranges3:
    max_num = ranges2[min_num] 
    if type(max_num) == list:
        max_num = int(ranges2[min_num][0])
        del ranges2[min_num][0]
    if min_num >= prev_max:
        total += max_num - min_num
    elif max_num < prev_max:
        total += 0
    elif min_num < prev_max:
        total += max_num - min_num - (prev_max - min_num)
    elif min_num == prev_max:
        total += max_num - min_num
    
    prev_min = min_num
    prev_max = max(prev_max, max_num)
    # print(min_num, max_num, total)



print(total)