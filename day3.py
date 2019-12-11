# problem 1
import sys


def closest_intersection2(wires):
    visited_locs = {}
    intersections = []

    # walk through each wire
    wireIdx = 0
    for wire in wires:
        x = y = 0
        for vector in wire:
            direction = vector[0]
            steps = int(vector[1:])

            while steps > 0:
                if direction == "U":
                    y += 1
                elif direction == "D":
                    y -= 1
                elif direction == "L":
                    x -= 1
                elif direction == "R":
                    x += 1

                steps -= 1
                loc = str(x) + " " + str(y)
                if loc in visited_locs and wireIdx not in visited_locs[loc]:
                    intersections.append([x, y])
                    visited_locs[loc].append(wireIdx)
                else:
                    visited_locs[loc] = [wireIdx]

        wireIdx += 1

    shortest_path = sys.maxsize
    for x in intersections:
        if distance(x) < shortest_path:
            shortest_path = distance(x)

    return shortest_path


def closest_intersection(wires):
    paths = []
    for wire in wires:
        paths.append(build_path(wire))

    intersections = find_intersections(paths)

    shortest_path = sys.maxsize
    for x in intersections:
        if distance(x) < shortest_path:
            shortest_path = distance(x)

    return shortest_path


def build_path(wire):
    path = []
    x = 0
    y = 0

    for vector in wire:
        direction = vector[0]
        steps = int(vector[1:])

        while steps > 0:
            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "L":
                x -= 1
            elif direction == "R":
                x += 1

            steps -= 1
            path.append([x, y])

    return path


def find_intersections(paths):
    intersections = []

    for loc in paths[0]:
        if loc in paths[1]:
            intersections.append(loc)

    return intersections


def distance(location):
    return abs(location[0]) + abs(location[1])


##### file reading
# format the input file
wires_txt = open("./day3_input.txt")
wires = wires_txt.readlines()
wires_txt.close()

# break apart each sublist
for idx in range(len(wires)):
    wires[idx] = wires[idx].strip().split(",")

##### testing
print(closest_intersection2(wires))

"""notepad
old way => [
    [[0,1], [0,2]],
    [[1,1], [0,3]]
]

nested loop to find intersections => [
    [0,1], [2,3]
]

go through each intersection to find shortest distance

new way => {
    '0 1': 2,
    '0 2': 1
}

take note of combinations that have been set already
because this is an intersection

"""
