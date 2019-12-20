import math


def intcode_computer(instructions, phase_setting=-1, prev_input=-1):
    # start pointer at beginning of instructions
    pointer = 0
    # run the instructions until exit code encountered (99)
    while instructions[pointer] != 99:
        # determine the instruction
        current_instruction = instructions[pointer] % 10

        # capture the mode settings from the instruction
        modes = math.floor(instructions[pointer] / 100)

        # 01: add first and second parameter, store at third parameter (step: 4)
        # 02: mult first and second parameter, store at third parameter (step: 4)
        # 03: take input and store at location of only parameter (step: 2)
        # 04: print value at location of only parameter (step: 2)

        # 05: if the first parameter is non-zero, set instruction pointer to parameter 2
        # 06: if the first parameter is zero, set instruction pointer to parameter 2
        # 07: if first param is less than the second param, store 1 at position
        # of third param, otherwise 0
        # 08: if first and second param are equal, store 1 at position of third
        # parameter, otherwise 0
        if current_instruction == 1:
            left_operand = 0
            right_operand = 0

            if modes % 10 == 0:
                left_operand = instructions[instructions[pointer + 1]]
            elif modes % 10 == 1:
                left_operand = instructions[pointer + 1]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if math.floor(modes % 100 / 10) == 0:
                right_operand = instructions[instructions[pointer + 2]]
            elif math.floor(modes % 100 / 10) == 1:
                right_operand = instructions[pointer + 2]
            else:
                print("ERROR: Parameter mode unknown")
                return

            instructions[instructions[pointer + 3]] = left_operand + right_operand

            pointer += 4
        elif current_instruction == 2:
            left_operand = 0
            right_operand = 0

            if modes % 10 == 0:
                left_operand = instructions[instructions[pointer + 1]]
            elif modes % 10 == 1:
                left_operand = instructions[pointer + 1]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if math.floor(modes % 100 / 10) == 0:
                right_operand = instructions[instructions[pointer + 2]]
            elif math.floor(modes % 100 / 10) == 1:
                right_operand = instructions[pointer + 2]
            else:
                print("ERROR: Parameter mode unknown")
                return

            instructions[instructions[pointer + 3]] = left_operand * right_operand

            pointer += 4
        elif current_instruction == 3:
            if phase_setting != -1:
                t = phase_setting
                phase_setting = -1
            elif prev_input != -1:
                t = prev_input
            else:
                t = int(input("Enter your input: "))
            instructions[instructions[pointer + 1]] = t
            pointer += 2
        elif current_instruction == 4:
            if modes % 10 == 0:
                return instructions[instructions[pointer + 1]]
                # print(instructions[instructions[pointer + 1]])
            elif modes % 10 == 1:
                return instructions[pointer + 1]
                # print(instructions[pointer + 1])
            else:
                print("ERROR: Parameter mode unknown")
                return
            pointer += 2
        elif current_instruction == 5:
            first_val = 0
            second_val = 0

            if modes % 10 == 0:
                first_val = instructions[instructions[pointer + 1]]
            elif modes % 10 == 1:
                first_val = instructions[pointer + 1]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if math.floor(modes % 100 / 10) == 0:
                second_val = instructions[instructions[pointer + 2]]
            elif math.floor(modes % 100 / 10) == 1:
                second_val = instructions[pointer + 2]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if first_val != 0:
                pointer = second_val
            else:
                pointer += 3
        elif current_instruction == 6:
            first_val = 0
            second_val = 0

            if modes % 10 == 0:
                first_val = instructions[instructions[pointer + 1]]
            elif modes % 10 == 1:
                first_val = instructions[pointer + 1]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if math.floor(modes % 100 / 10) == 0:
                second_val = instructions[instructions[pointer + 2]]
            elif math.floor(modes % 100 / 10) == 1:
                second_val = instructions[pointer + 2]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if first_val == 0:
                pointer = second_val
            else:
                pointer += 3
        elif current_instruction == 7:
            first_val = 0
            second_val = 0

            if modes % 10 == 0:
                first_val = instructions[instructions[pointer + 1]]
            elif modes % 10 == 1:
                first_val = instructions[pointer + 1]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if math.floor(modes % 100 / 10) == 0:
                second_val = instructions[instructions[pointer + 2]]
            elif math.floor(modes % 100 / 10) == 1:
                second_val = instructions[pointer + 2]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if first_val < second_val:
                instructions[instructions[pointer + 3]] = 1
            else:
                instructions[instructions[pointer + 3]] = 0

            pointer += 4
        elif current_instruction == 8:
            first_val = 0
            second_val = 0

            if modes % 10 == 0:
                first_val = instructions[instructions[pointer + 1]]
            elif modes % 10 == 1:
                first_val = instructions[pointer + 1]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if math.floor(modes % 100 / 10) == 0:
                second_val = instructions[instructions[pointer + 2]]
            elif math.floor(modes % 100 / 10) == 1:
                second_val = instructions[pointer + 2]
            else:
                print("ERROR: Parameter mode unknown")
                return

            if first_val == second_val:
                instructions[instructions[pointer + 3]] = 1
            else:
                instructions[instructions[pointer + 3]] = 0

            pointer += 4
        else:
            print(f"ERROR: Instruction unknown {current_instruction}")
            return


def generate_permutations(list, left, right, perms=[]):
    if left == right:
        perms.append(tuple(list))
    else:
        for i in range(left, right + 1):
            list[left], list[i] = list[i], list[left]
            generate_permutations(list, left + 1, right, perms)
            list[left], list[i] = list[i], list[left]

    return perms


# Day 7, Problem 1
def init_amplifiers(instructions):
    # determine all permutations of 0-4
    phase_settings = generate_permutations([0, 1, 2, 3, 4], 0, 4)

    # test each one with intcode computer
    highest_output = -1

    for combination in phase_settings:
        instructions_copy = instructions.copy()

        input_signal = 0
        for setting in combination:
            new_input_signal = intcode_computer(
                instructions_copy, setting, input_signal
            )
            input_signal = new_input_signal

        highest_output = max(highest_output, input_signal)

    # return the highest result
    return highest_output


# Day 7, Problem 2
# this problem will require building out an amplifier class to have some sense
# of state


# read file
txt_file = open("./day7_input.txt")
opcodes_txt = txt_file.readline()
txt_file.close()

# format the codes into a list
instructions = opcodes_txt.strip().split(",")
for i in range(len(instructions)):
    instructions[i] = int(instructions[i])

# send the codes to the intcode computer
print(init_amplifiers(instructions))

# test
# 4 3 2 1 0
# s1 = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
# print(intcode_computer(s1))
