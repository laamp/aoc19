##### problem 1
import sys

##### version 2
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


##### version 1
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


##### problem 2
def shortest_intersection(wires):
    visited_locs = {}  # k = location, v = list of lists [wireIdx, steps(length)]
    shortest_connection = (
        sys.maxsize
    )  # keep track of shortest intersection found so far

    # walk through wires
    wireIdx = 0
    for wire in wires:
        x = y = 0  # location tracker
        length = 0  # current length of the current wire
        for vector in wire:
            direction = vector[0]  # wire's current heading
            steps = int(vector[1:])  # steps remaining at this heading

            while steps > 0:
                # update position
                if direction == "U":
                    y += 1
                elif direction == "D":
                    y -= 1
                elif direction == "L":
                    x -= 1
                elif direction == "R":
                    x += 1

                # decrease steps, increase length
                steps -= 1
                length += 1

                current_loc = str(x) + " " + str(y)
                if current_loc in visited_locs:
                    if visited_locs[current_loc][1] + length < shortest_connection:
                        shortest_connection = visited_locs[current_loc][1] + length
                else:
                    visited_locs[current_loc] = [wireIdx, length]

        # move to next wire
        wireIdx += 1

    return shortest_connection


##### file reading
# format the input file
wires_txt = open("./day3_input.txt")
wires = wires_txt.readlines()
wires_txt.close()

# break apart each sublist
for idx in range(len(wires)):
    wires[idx] = wires[idx].strip().split(",")

##### testing
# print(closest_intersection2(wires))
print(shortest_intersection(wires))

##### notepad
"""
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

problem 2:

data from problem 1: dict = {
    '0 1': [0, 1],
    etc...
}
key is the location
value is list of wires that exist in that location

data in problem 2 will need to look like: dict = {
    '0 1': [[wireIdx, length so far]]
}

"""
