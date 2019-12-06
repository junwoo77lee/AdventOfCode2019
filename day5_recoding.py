# For Day2 re-coding
from typing import List
from itertools import permutations



def computing_machine(intcode: str) -> int:
    code_list = parse_code(intcode)

    i = 0
    while code_list[i] != 99:
        opcode = code_list[i]
        opcode, *modes = parse_opcode(opcode) # returns modes and new_opcode
        code_list, i = processor(opcode, code_list, i, input=5, parsed_modes=modes)

    return code_list


def parse_opcode(opcode: int) -> List[int]:
    five_digits_opcode = str(opcode).zfill(5)
    mode3, mode2, mode1, _, opcode = list(five_digits_opcode)
    return [int(opcode), int(mode1), int(mode2), int(mode3)]


def sub_processor(code_list: List[int], index: int, n: int, parsed_modes: List[int], target: bool) -> List[int]:
    # return the converted paramaters according to each parameter mode

    params = code_list[index+1:index+n+1]
    if target:
        parsed_modes[-1] = 1

    new_params = []
    for m, p in zip(parsed_modes, params):
        if m == 0: # position mode
            p = code_list[p]
            new_params.append(p)
        else: # immediate mode
            p = p
            new_params.append(p)

    return new_params


def processor(opcode: int, code_list: List[int], index: int, *, input: int, parsed_modes: List[str]) -> (List[int], int):
    # return the modified list
    index_ref = dict(zip([1, 2, 3, 4, 5, 6, 7, 8], [4, 4, 2, 2, 3, 3, 4, 4]))

    if opcode == 1:
        params = sub_processor(code_list, index, 3, parsed_modes, True)
        code_list[params[2]] = params[0] + params[1]
        index += index_ref[opcode]

    elif opcode == 2:
        params = sub_processor(code_list, index, 3, parsed_modes, True)
        code_list[params[2]] = params[0] * params[1]
        index += index_ref[opcode]

    elif opcode == 3:
        param1 = code_list[index + 1]
        code_list[param1] = input
        index += index_ref[opcode]

    elif opcode == 4:
        params = sub_processor(code_list, index, 1, parsed_modes, False)
        output = params[0]
        print(f'Output: {output}')
        index += index_ref[opcode]
    
    elif opcode == 5:
        params = sub_processor(code_list, index, 2, parsed_modes, False)
        if params[0] != 0:
            index = params[1]
        else:
            index += index_ref[opcode]

    elif opcode == 6:
        params = sub_processor(code_list, index, 2, parsed_modes, False)
        if params[0] == 0:
            index = params[1]
        else:
            index += index_ref[opcode]

    elif opcode == 7:
        params = sub_processor(code_list, index, 3, parsed_modes, True)
        if params[0] < params[1]:
            code_list[params[2]] = 1
        else:
            code_list[params[2]] = 0
        index += index_ref[opcode]
        
    elif opcode == 8:
        params = sub_processor(code_list, index, 3, parsed_modes, True)
        if params[0] == params[1]:
            code_list[params[2]] = 1
        else:
            code_list[params[2]] = 0
        index += index_ref[opcode]

    return code_list, index
    

def parse_code(intcode: str) -> List[int]:
    return [int(el.strip()) for el in intcode.split(',')]


# unit test
# T1 = "1,9,10,3,2,3,11,0,99,30,40,50"
# T2 = "1,0,0,0,99"
# T3 = "2,3,0,3,99"
# T4 = "2,4,4,5,99,0"
# T5 = "1,1,1,4,99,5,6,0,99"

# TEST = [T1, T2, T3, T4, T5]
# for test in TEST:
#     print(computing_machine(test))


# part1 = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0"
# print(f"part1: {computing_machine(part1)[0]}")

# # day2 part2
# with open('data/day2.txt') as f:
#     intcode = f.read()

# for noun, verb in permutations(range(100), 2):
#     output = computing_machine(intcode, noun, verb)[0]
#     if output == 19690720:
#         print(100 * noun + verb)
#         break


# Day5

# T1 = "3,0,4,0,99"
# print(computing_machine(T1))

# # Part I
with open('data/day5.txt') as f:
    intcode = f.read()
# print(computing_machine(intcode))

# Part II

# T2 = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
# print(computing_machine(T2))
print(computing_machine(intcode))


