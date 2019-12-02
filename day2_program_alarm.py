from itertools import permutations
from typing import List

# PART I
# make a working computer

RAW = [int(code) for code in "1,9,10,3,2,3,11,0,99,30,40,50".split(',')]


def working_computer(intcode: List[int]) -> List[int]:

    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if not opcode == 99:
            input1 = intcode[i+1]
            input2 = intcode[i+2]
            target = intcode[i+3]

            if opcode == 1:
                intcode[target] = intcode[input1] + \
                    intcode[input2]
            elif opcode == 2:
                intcode[target] = intcode[input1] * \
                    intcode[input2]
        else:
            return intcode


assert working_computer(RAW) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
assert working_computer([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert working_computer([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert working_computer([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert working_computer([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
    30, 1, 1, 4, 2, 5, 6, 0, 99]

with open('data/day2.txt') as f:
    line = f.readline()
    real_intcode = [int(code) for code in line.split(',')]

# print(working_computer(real_intcode))


# PART II

for noun, verb in permutations(range(3, 100), 2):
    with open('data/day2.txt') as f:
        real_intcode = f.read()
    intcode_list = [int(integer) for integer in real_intcode.split(',')]
    intcode_list[1] = noun
    intcode_list[2] = verb
    if working_computer(intcode_list)[0] == 19690720:
        print(f'noun: {noun}, verb: {verb}')
        print(f'{noun * 100 + verb}')
