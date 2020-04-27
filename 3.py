f = open("./3-input.txt", "r")
lines = f.readlines()

wire_1 = lines[0].split(",")
wire_2 = lines[1].split(",")

# wire_1 = "R8,U5,L5,D3".split(",")
# wire_2 = "U7,R6,D4,L4".split(",")


def manhattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


path = {}
last_coordinate = [0, 0]
steps_offset = 0
for command in wire_1:
    c = command[0]
    steps = int(command[1:])

    for step in range(1, steps + 1):
        if c == "R":
            last_coordinate = [last_coordinate[0] + 1, last_coordinate[1]]
        elif c == "L":
            last_coordinate = [last_coordinate[0] - 1, last_coordinate[1]]
        elif c == "U":
            last_coordinate = [last_coordinate[0], last_coordinate[1] + 1]
        else:
            last_coordinate = [last_coordinate[0], last_coordinate[1] - 1]

        # print(last_coordinate, c)
        path[str(last_coordinate)] = step + steps_offset

    steps_offset += steps

min_steps = 10000000
last_coordinate = [0, 0]
steps_offset = 0
for command in wire_2:
    c = command[0]
    steps = int(command[1:])

    for step in range(1, steps + 1):
        if c == "R":
            last_coordinate = [last_coordinate[0] + 1, last_coordinate[1]]
        elif c == "L":
            last_coordinate = [last_coordinate[0] - 1, last_coordinate[1]]
        elif c == "U":
            last_coordinate = [last_coordinate[0], last_coordinate[1] + 1]
        else:
            last_coordinate = [last_coordinate[0], last_coordinate[1] - 1]

        # print(last_coordinate, c)
        if str(last_coordinate) in path:
            steps_till_now = steps_offset + step
            min_steps = min(min_steps, steps_till_now +
                            path[str(last_coordinate)])

    steps_offset += steps

print(min_steps)
