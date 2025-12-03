data = open("day3/day3.txt", "r").readlines()
# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".splitlines()

data = [[int(x) for x in el.strip()] for el in data]
tot = 0

curr_joltage = []
curr_ind = -1

for line in data:
    curr_joltage = []
    curr_ind = -1
    total = len(line)
    for i in range(1, 13):
        joltage0 = max(line[curr_ind+1:total-12+i])
        curr_ind = (line[curr_ind+1:total-12+i]).index(joltage0) + curr_ind + 1
        curr_joltage.append(joltage0)

    num = int("".join([str(i) for i in curr_joltage]))
    print(num)
    tot += num




print(tot)
