import time
# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............""".splitlines()

# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............""".splitlines()


data = [i.strip() for i in open("day7\day7.txt", "r").readlines()]

count = 0
grid = [[i for i in el] for el in data]
grid_acc_weighted = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
splits = 0
timelines = 1

def continue_beam(pos, path):
    global splits, timelines, start, prev
    # [print(*line) for line in grid_acc_weighted]
    # [print(*line) for line in grid]

    path.append(pos)

    # if time.time() - start > prev + 1:
    #     prev += 1 
    #     with open("out.txt", "w") as f:
    #         for line in grid:
    #             f.write("".join(line)+"\n")

    if pos[0] == len(grid) - 1:
        return
    if grid[pos[0] + 1][pos[1]] == ".":
        grid[pos[0] + 1][pos[1]]  = "|"
        continue_beam((pos[0] + 1, pos[1]), path)
    elif grid[pos[0] + 1][pos[1]] == "|":
        for el in path:
            # print(el)
            x, y = el[0], el[1]
            grid_acc_weighted[x][y] += grid_acc_weighted[pos[0] + 1][pos[1]]
        timelines += grid_acc_weighted[pos[0] + 1][pos[1]] 
    elif grid[pos[0] + 1][pos[1]] == "^":
        # grid[pos[0] + 1][pos[1]] = ">"
        splits += 1
        timelines += 1
        for el in path:
            # print(el)
            x, y = el[0], el[1]
            grid_acc_weighted[x][y] += 1

        
        grid[pos[0]+1][pos[1] + 1] = "|"
        grid[pos[0]+1][pos[1] - 1] = "|"
        print(splits)
        # [print(*line) for line in grid_acc_weighted]
        # [print(*line) for line in grid]
        # input()

        path2 = list(path)
        continue_beam((pos[0]+1, pos[1] - 1), path)
        continue_beam((pos[0]+1, pos[1] + 1), path2)
        
    # elif grid[pos[0] + 1][pos[1]] == ">":
    #     grid[pos[0]][pos[1] + 1] == "|"
    #     grid[pos[0]][pos[1] - 1] == "|"
    #     continue_beam((pos[0], pos[1] - 1))
    #     continue_beam((pos[0], pos[1] + 1))
    

start = time.time()
prev = 0
continue_beam((0, len(grid[0])//2), [])
# [print(*line) for line in grid_acc_weighted]
# [print(*line) for line in grid]
print(splits, timelines)


    

