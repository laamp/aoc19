# Day 6 / Problem 1
def orbit_map(list_of_orbits):
    # dict to store all planets with the planets that orbit them
    master_planet_dict = {}

    # convert list of orbits into master dict
    for orbit in list_of_orbits:
        orbit_split = orbit.split(")")

        # if we've seen this planet before
        if master_planet_dict.get(orbit_split[0]) != None:
            master_planet_dict[orbit_split[0]].append(orbit_split[1])
        else:
            master_planet_dict[orbit_split[0]] = [orbit_split[1]]

    return master_planet_dict


def total_orbits(orbit_dict):
    total = 0

    # calculate direct and indirect orbits for each planet
    for key in orbit_dict:
        total += get_orbits(key, orbit_dict)

    return total


def get_orbits(current, orbit_dict):
    # planet has nothing orbiting it
    if orbit_dict.get(current) == None:
        return 0

    count = 0

    # perform same calc for each subsequent planet in orbit around this one
    for planet in orbit_dict[current]:
        count += get_orbits(planet, orbit_dict)

    # return all orbits of this planet plus its children
    return count + len(orbit_dict[current])


# Day 6 / Problem 2
def path_to_santa(orbit_dict):
    # find planet that "YOU" is orbiting
    my_location = None
    for key in orbit_dict:
        if "YOU" in orbit_dict[key]:
            my_location = key
            break

    return distance_to_santa(my_location, orbit_dict)


def distance_to_santa(current_loc, orbit_dict, counter=0, checked=[]):
    # keep track of planets checked
    checked.append(current_loc)

    # does this current planet have SAN?
    if orbit_dict.get(current_loc) != None:
        if "SAN" in orbit_dict[current_loc]:
            return counter
    elif orbit_dict.get(current_loc) == None:
        return -1

    # get list of neighboring planets to check
    downstream = []
    for planet in orbit_dict[current_loc]:
        if planet != "YOU" and planet not in checked:
            downstream.append(planet)

    # get planet that this one is orbiting
    upstream = []
    for key in orbit_dict:
        if current_loc in orbit_dict[key] and key not in checked:
            upstream.append(key)

    # check orbiting planet
    if len(upstream) == 0:
        left_result = -1
    else:
        left_result = distance_to_santa(upstream[0], orbit_dict, counter + 1, checked)

    # check neighboring planets
    if len(downstream) == 0:
        right_result = -1
    else:
        right_result = -1
        for p in downstream:
            result = distance_to_santa(p, orbit_dict, counter + 1, checked)
            right_result = max(right_result, result)

    return max(left_result, right_result)


# read file
txt_file = open("./day6_input.txt")
orbits_txt = txt_file.read().splitlines()
txt_file.close()

# testing
# small_sample = [
#     "COM)B",
#     "B)C",
#     "C)D",
#     "D)E",
#     "E)F",
#     "B)G",
#     "G)H",
#     "D)I",
#     "E)J",
#     "J)K",
#     "K)L",
# ]
# result = orbit_map(small_sample)
# print(result)
# print(total_orbits(result))

# sample2 = [
#     "COM)B",
#     "B)C",
#     "C)D",
#     "D)E",
#     "E)F",
#     "B)G",
#     "G)H",
#     "D)I",
#     "E)J",
#     "J)K",
#     "K)L",
#     "K)YOU",
#     "I)SAN",
# ]
# d = orbit_map(sample2)
# print(path_to_santa(d))

# run program
result = orbit_map(orbits_txt)
# print(total_orbits(result))
print(path_to_santa(result))

"""
"""
