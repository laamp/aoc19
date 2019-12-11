##### problem 1
def pw_solver(custom_range):
    possible_answers = 0

    for n in custom_range:

        idx = 0
        double_found = False
        decrease_encountered = False
        for digit in str(n):
            if idx + 1 < len(str(n)):
                if str(n)[idx] == str(n)[idx + 1]:
                    double_found = True

                if str(n)[idx] > str(n)[idx + 1]:
                    decrease_encountered = True

            idx += 1

        if double_found and not decrease_encountered:
            possible_answers += 1

    return possible_answers


##### problem 2
def pw_solver2(custom_range):
    answers = 0

    # loop for each number in the range
    for num in custom_range:
        n = str(num)
        decreasing = False
        double = False
        i = 0

        # loop for each digit in the number
        while i in range(len(n)):
            # check that the digits aren't decreasing
            if i + 1 < len(n) and n[i] > n[i + 1]:
                decreasing = True

            # identify that there is a potential double if we haven't found one yet
            if not double:
                if i + 1 < len(n) and n[i] == n[i + 1]:
                    # we have a double
                    double = True

                    # check potential left neighbor
                    if i - 1 >= 0 and n[i] == n[i - 1]:
                        double = False

                    # check potential right neighbor
                    if i + 2 < len(n) and n[i] == n[i + 2]:
                        double = False

            i += 1

        # add this answer if validation passed
        if double and not decreasing:
            answers += 1

    return answers


##### testing
puzzle_input = range(125730, 579381)

print(pw_solver(puzzle_input))
print(pw_solver2(puzzle_input))

##### notepad
"""
the double stays if the neighbors aren't the same digits
"""
