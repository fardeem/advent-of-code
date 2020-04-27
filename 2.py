f = open('./2-input.txt', 'r')
lines = f.readline()


def get_memory():
    return [int(a) for a in lines.split(",")]


def program(commands):
    i = 0
    while i < len(commands):
        if commands[i] == 1:
            commands[commands[i + 3]] = commands[commands[i + 1]] + \
                commands[commands[i + 2]]
            i += 4
        elif commands[i] == 2:
            commands[commands[i + 3]] = commands[commands[i + 1]] * \
                commands[commands[i + 2]]
            i += 4
        elif commands[i] == 99:
            break
        else:
            continue

    return commands


for noun in range(99):
    for verb in range(99):
        commands = get_memory()
        commands[1] = noun
        commands[2] = verb
        output = program(commands)[0]

        if output == 19690720:
            print(100 * noun + verb)
            break

# print(program(commands))
