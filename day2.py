# problem 1
def program(codes):
    idx = 0
    while idx < len(codes):
        # exit on opcode 99
        if codes[idx] == 99:
            return

        # opcode 1 is addition, opcode 2 is multiplication
        if codes[idx] == 1:
            codes[codes[idx + 3]] = codes[codes[idx + 1]] + codes[codes[idx + 2]]
        elif codes[idx] == 2:
            codes[codes[idx + 3]] = codes[codes[idx + 1]] * codes[codes[idx + 2]]
        else:
            print("Something went wrong, ERROR: {}".format(codes[idx]))

        # step by 4
        idx += 4


# problem 2
def program2(codes):
    MAGIC_NUMBER = 19690720

    for i in range(0, 100):
        for j in range(0, 100):
            new_list = codes.copy()
            new_list[1] = i
            new_list[2] = j
            program(new_list)

            if new_list[0] == MAGIC_NUMBER:
                print(f"100 * i={i} + j={j} = {100 * i + j}")


# read file
txt_file = open("./day2_input.txt")
opcodes_txt = txt_file.readline()
txt_file.close()

# format list to be ints
opcodes_list = opcodes_txt.strip().split(",")
for idx in range(len(opcodes_list)):
    opcodes_list[idx] = int(opcodes_list[idx])

# input instructions
# "noun"
# opcodes_list[1] = 12
# "verb"
# opcodes_list[2] = 2

# run program
# program(opcodes_list)
# print(opcodes_list)

program2(opcodes_list)
