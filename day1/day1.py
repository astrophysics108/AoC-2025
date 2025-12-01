data = open("day1/day1.txt", "r").readlines()
data = [x.strip() for x in data]

# data = """L68
# L30
# R48
# L100
# L1000
# L5
# R60
# L55
# L1
# L99
# R14
# R1000
# L82""".splitlines()

counter = 50
out = 0
past = 50
for line in data:
    if line.startswith("L"):
        counter -= int(line[1:])
    else:
        counter += int(line[1:])

    if past < counter:
        for i in range(past+1, counter+1):
            if i % 100 == 0:
                out += 1
    else:
         for i in range(counter, past):
            if i % 100 == 0:
                out += 1
    past = counter

    print(line, out)


print(out)