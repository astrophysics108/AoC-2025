from itertools import combinations_with_replacement
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np
import collections as col

data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".splitlines()

# data = [el.strip() for el in open("day10/input.txt", "r").readlines()]

def get_button_presses(line):
    line = line.split()
    buttons = [[int(x) for x in el[1:-1].split(",")] for el in line[1:-1]]
    # to_press = [x for x in line[0][1:-1]]
    joltage_to_press = [int(x) for x in line[-1][1:-1].split(",")]
    
    # for i, el in enumerate(to_press):
    #     if el == ".":
    #         to_press[i] = 0
    #     else:
    #          to_press[i] = 1

    # for i in range(1, 100):
    #     for x in combinations_with_replacement(buttons, i):
    #         # x = [tuple(a) for a in x]
    #         # perf = [tuple(a) for a in [[3], [1,3], [1,3], [1,3], [2,3], [2,3], [2,3], [0,2], [0,1], [0,1]]]
    #         # if col.Counter(x) == col.Counter(perf):
    #         #     print("yay")
    #         # state = list([0])*len(to_press)
    #         joltage = list([0])*len(joltage_to_press)
    #         for button in x:
    #             if x.count(button)%2 == 0:
    #                 break
    #             for num in button:
    #                 # state[num] =  (state[num] + 1)%2
    #                 joltage[num] += 1
    #         if joltage == joltage_to_press:
    #             print(i)
    #             return i
    #         # else:
    #         #     # print(i)
    #         #     ...

    for i, button in enumerate(buttons):
        new_button = list([0]) * len(joltage_to_press)
        for num in button:
            new_button[num] = 1
        buttons[i] = new_button


    buttons_new = np.array(buttons).T

    constraint = LinearConstraint(buttons_new, joltage_to_press, joltage_to_press)
    minim=np.ones(buttons_new.shape[1])
    inequalities = Bounds([0] * buttons_new.shape[1], [np.inf]*buttons_new.shape[1])
    more_constraints_yayayayay = np.ones(len(buttons), dtype=int)
    print("hi")
    print(buttons_new.shape, len(joltage_to_press), len(minim))
    res = milp(c=minim, constraints=[constraint], bounds=inequalities, integrality=more_constraints_yayayayay)
    return res.fun


tot = 0 
for line in data:
    tot += get_button_presses(line)

print(tot)
    

