import numpy as np

# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """.splitlines()

data = [el.strip() for el in open("day6/day6.txt", "r").readlines()]

homework = []
ops = []

# for line in data:
#     if line != data[-1]:
#         if line != data[0]:
#             for i, el in enumerate(line.split()):
#                 homework[i].append(el)
#         else:
#             for i, el in enumerate(line.split()):
#                 homework.append([el])
#     else:
#         ops = [i for i in line.split()]

for line in data:
    if line != data[-1]:
        if line != data[0]:
            for i, el in enumerate(line):
                homework[i].append(el)
        else:
            for i, el in enumerate(line):
                homework.append([el])
    else:
        ops = [i for i in line.split()]


print(homework, ops)

def p1():
    
    total = 0
    for i, el in enumerate(homework):
        if ops[i] == "+":
            total += sum([int(a) for a in el])
        else:
            x = 1
            for j in el:
                x *= int(j)

            total += x
    
    print(total)

def p2():

    total = 0
    count = 0
    acc_hw = []
    for i, el in enumerate(homework):
        if el == [" "]*len(el):
            if ops[count] == "+":
                total += sum([int(a) for a in acc_hw])
                print(sum([int(a) for a in acc_hw]), acc_hw)
            else:
                x = 1
                for j in acc_hw:
                    x *= int(j)

                print(x, acc_hw)
                total += x
            acc_hw = []
            count += 1
        else:
            acc_hw.append(int("".join(el)))

    if ops[count] == "+":
                total += sum([int(a) for a in acc_hw])
                print(sum([int(a) for a in acc_hw]), acc_hw)
    else:
                x = 1
                for j in acc_hw:
                    x *= int(j)

                print(x, acc_hw)
                total += x
        
    print(total)
        


                


p2()

