
import numpy as np
from typing import Iterable
from collections import defaultdict

T1 = "123456789012"

with open('data/day8.txt') as f:
    line = f.read()

def generate_layers(input: str, wide: int, tall: int) -> Iterable:
    input = list(input) #[int(number) for number in input]
    np_array = np.array(input).reshape(len(input)//(tall * wide) , tall, wide)
    return np_array

zeros, ones, twos = [], [], []
for layer in generate_layers(line, 25, 6):
    flatten = np.ravel(layer)
    zeros.append(sum(1 for num in flatten if num == '0'))
    ones.append(sum(1 for num in flatten if num == '1'))
    twos.append(sum(1 for num in flatten if num == '2'))

min_index = zeros.index(min(zeros))
ans = ones[min_index] * twos[min_index]
# print(zeros)
# print(ones)
# print(twos)
# print(ans)


# Part II
# T2 = "0222112222120000"
# p2_test = generate_layers(T2, 2, 2)

p2_real = generate_layers(line, 25, 6)
# print(p2_real)
all_dict = defaultdict(list)
for t in range(6):
    for w in range(25):
        for layer in p2_real:
            # print(layer)
            all_dict[(t, w)].append(layer[t, w])
            # print(all_dict)

# print(all_dict)
result_dict = defaultdict(list)
for k, v in all_dict.items():
    i = 0
    while i < len(v):
        if v[i] != '2':
            result_dict[k].append(v[i])
            break
        i += 1

new_list = []
for v in result_dict.values():
    new_list.append(v)

print(np.array(new_list).reshape(6,25))

ans = """
[['1' '0' '0' '1' '0' '0' '1' '1' '0' '0' '1' '1' '1' '0' '0' '0' '1' '1' '0' '0' '1' '1' '1' '1' '0']
 ['1' '0' '0' '1' '0' '1' '0' '0' '1' '0' '1' '0' '0' '1' '0' '1' '0' '0' '1' '0' '1' '0' '0' '0' '0']
 ['1' '1' '1' '1' '0' '1' '0' '0' '0' '0' '1' '1' '1' '0' '0' '1' '0' '0' '0' '0' '1' '1' '1' '0' '0']
 ['1' '0' '0' '1' '0' '1' '0' '1' '1' '0' '1' '0' '0' '1' '0' '1' '0' '0' '0' '0' '1' '0' '0' '0' '0']
 ['1' '0' '0' '1' '0' '1' '0' '0' '1' '0' '1' '0' '0' '1' '0' '1' '0' '0' '1' '0' '1' '0' '0' '0' '0']
 ['1' '0' '0' '1' '0' '0' '1' '1' '1' '0' '1' '1' '1' '0' '0' '0' '1' '1' '0' '0' '1' '0' '0' '0' '0']]
 """

        



