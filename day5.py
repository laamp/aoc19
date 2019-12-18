import math

# Day 5 / Problem 1 & Problem 2
def intcode_computer(instructions):
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
            t = int(input("Enter your input: "))
            instructions[instructions[pointer + 1]] = t
            pointer += 2
        elif current_instruction == 4:
            if modes % 10 == 0:
                print(instructions[instructions[pointer + 1]])
            elif modes % 10 == 1:
                print(instructions[pointer + 1])
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


# read file
txt_file = open("./day5_input.txt")
opcodes_txt = txt_file.readline()
txt_file.close()

# format the codes into a list
instructions = opcodes_txt.strip().split(",")
for i in range(len(instructions)):
    instructions[i] = int(instructions[i])

# send the codes to the intcode computer
intcode_computer(instructions)

# test cases
# intcode_computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8])

"""
"""
