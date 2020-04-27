import math


def fuel_required(mass):
    return math.floor(mass / 3) - 2


f = open("./1-input.txt", "r")

total_fuel = 0
modules = f.readlines()
for mass in modules:
    total_fuel += fuel_required(int(mass))


print(total_fuel)
