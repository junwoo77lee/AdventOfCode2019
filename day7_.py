# For Day2 re-coding
from typing import List
from itertools import permutations


AMP = ['A', 'B', 'C', 'D', 'E']

def run_amplifier(intcode: str, phase_sequence: List[int]) -> int:

    cycle = 0
    while True:
        if cycle == 0:
            print(f"Cycle: {cycle}")
            for i, phase in enumerate(phase_sequence):
                print(f"AMP: {AMP[i]}")
                if i == 0:
                    output_from_previous_amp = computing_machine(intcode, [phase, 0])
                else:
                    output_from_previous_amp = computing_machine(intcode, [phase, output_from_previous_amp])
                print(f"AMP: {AMP[i]} done, the output: {output_from_previous_amp}")
            print(f"Cycle: {cycle} done.")

        cycle += 1

    return output_from_previous_amp


def computing_machine(intcode: str, input_list: List[int]) -> int:
    code_list = parse_code(intcode)
    # output = []
    output = 0
    i = 0
    while True:
        opcode = code_list[i]
        if opcode == 99:
            break
        opcode, *modes = parse_opcode(opcode) # returns modes and new_opcode
        print(f'opcode: {opcode}')
        code_list, i, output = processor(opcode, code_list, i, input_list, output=output, parsed_modes=modes)

    return output


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


def processor(opcode: int, code_list: List[int], index: int, input_list: List[int], *, output: List[int], parsed_modes: List[str]) -> (List[int], int):
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
        print(input_list)
        code_list[param1] = input_list.pop(0)
        index += index_ref[opcode]

    elif opcode == 4:
        params = sub_processor(code_list, index, 1, parsed_modes, False)
        # output.append(params[0])
        output = params[0]
        print(f"Output: {output}")
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

    return code_list, index, output
    

def parse_code(intcode: str) -> List[int]:
    return [int(el.strip()) for el in intcode.split(',')]


# Part I
# T1 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
# T2 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
# T3 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
# print(run_amplifier(T3, [1,0,4,3,2]))

with open('data/day7.txt') as f:
    program = f.read()

# all_combinations = []
# for phase_sequence in permutations(range(5)):
#     signal = run_amplifier(program, phase_sequence)
#     all_combinations.append((phase_sequence, signal))
# print(max(all_combinations, key=lambda x: x[1]))


# Part II
T1 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
print(run_amplifier(T1, [9,8,7,6,5]))




    




