import math

# Day 5 / Problem 1
def intcode_computer(instructions):
    # start pointer at beginning of instructions
    pointer = 0
    # run the instructions until exit code encountered (99)
    while instructions[pointer] != 99:
        # move pointer based on what instruction is encountered
        step = 0

        # determine the instruction
        current_instruction = instructions[pointer] % 10

        # capture the mode settings from the instruction
        modes = math.floor(instructions[pointer] / 100)

        # 01: add first and second parameter, store at third parameter (step: 4)
        # 02: mult first and second parameter, store at third parameter (step: 4)
        # 03: take input and store at location of only parameter (step: 2)
        # 04: print value at location of only parameter (step: 2)
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

            step = 4
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

            step = 4
        elif current_instruction == 3:
            t = int(input("Enter your input: "))
            instructions[instructions[pointer + 1]] = t
            step = 2
        elif current_instruction == 4:
            if modes % 10 == 0:
                print(instructions[instructions[pointer + 1]])
            elif modes % 10 == 1:
                print(instructions[pointer + 1])
            else:
                print("ERROR: Parameter mode unknown")
                return
            step = 2
        else:
            print(f"ERROR: Instruction unknown {current_instruction}")
            return

        pointer += step


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

"""
"""
