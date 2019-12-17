from typing import List, Iterator, Tuple
from itertools import cycle


def pattern_generator(phase_id: int, numbers: str) -> Tuple[Iterator[int], List[int]]:
    interval = phase_id * 2
    basic_pattern = [0, 1, 0, -1]
    new_pattern = [n for n in basic_pattern for _ in range(phase_id) if n != 0]
    c = cycle(new_pattern) #; next(c)

    # print(list(range(phase_id - 1, interval - 1)))
    numbers_list = [int(num) for i, num in enumerate(list(numbers)) if i % interval in range(phase_id - 1, interval - 1)]
    # print(phase_id, interval, numbers_list)
    return c, numbers_list


# phase1: 1,  3,  5,  7, ... -> x2  => 0, 2, 4, 6,
# phase2: 2, 3,  6, 7, ... -> x4 => 1, 2,  5, 6
# phase3: 3, 4, 5,  9, 10, 11, ...  -> x6 => 2, 3, 4,  8, 9, 10
# phase4: 4, 5, 6, 7,  12, 13, 14, 15, ...  -> x8


def fft(numbers: str) -> str:
#    numbers = list(map(int, list(numbers)))
   n = len(numbers)
   digits = []
   for phase_id in range(1, n+1):
       patterns, numbers_list = pattern_generator(phase_id, numbers)
    #    print(phase_id, numbers)
       subtotal = 0
       for n, p in zip(numbers_list, patterns):
           subtotal += n * p
        #    print(n, p, subtotal)
       digits.append(str(subtotal)[-1])
    #    print(digits)
    #    print()

   return ''.join(digits)


def phase_fft(numbers: str, phase:int) -> str:

    for _ in range(phase):
        numbers = fft(numbers)
    return numbers


# assert phase_fft('12345678', 4) == '01029498'
# assert phase_fft('80871224585914546619083218645595', 100)[:8] == '24176176'
# assert phase_fft('19617804207202209144916044189917', 100)[:8] == '73745418'
# assert phase_fft('69317163492948606335995924319873', 100)[:8] == '52432133'

# print(phase_fft('80871224585914546619083218645595', 100))

with open('data/day16.txt') as f:
    numbers = f.read()

# print(phase_fft(numbers, 100)[:8])


def part2(numbers: str) -> List[int]:
    offset = int(numbers[:7])
    numbers = [int(num) for num in numbers] * 10_000

    assert offset > len(numbers) // 2

    for _ in range(100):
        pos = len(numbers) - 1
        total = 0

        while offset <= pos:
            total += numbers[pos]
            numbers[pos] = total % 10 if total > 0 else (total * -1) % 10
            pos -= 1
    
    return numbers[offset:offset+8]


print(part2(numbers))