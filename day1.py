import math


def fuel_counter_upper(input):
    total_fuel = 0

    for mass in input:
        total_fuel += math.floor(int(mass) / 3) - 2

    return total_fuel


def fuel_counter_upper2(input):
    total_fuel = 0

    for mass in input:
        total_fuel += fuel_calculator(int(mass))

    return total_fuel


def fuel_calculator(m):
    fuel = math.floor(m / 3) - 2

    if fuel < 1:
        return 0
    else:
        return fuel + fuel_calculator(fuel)


mass_list_txt = open("./day1_input.txt")
mass_list = mass_list_txt.readlines()
mass_list_txt.close()

print(fuel_counter_upper2(mass_list))
