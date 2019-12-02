# 1. take its mass
# 2. divide by three
# 3. round down
# 4. subtract 2
import math
from typing import List

# PART I


def find_required_fuel(mass: int) -> int:
    return math.floor(mass / 3) - 2


assert find_required_fuel(12) == 2
assert find_required_fuel(14) == 2
assert find_required_fuel(1969) == 654
assert find_required_fuel(100756) == 33583

with open('data/day1.txt') as f:
    fuels = [int(line.strip()) for line in f]

total_fules_requirment = sum(map(find_required_fuel, fuels))
print(total_fules_requirment)

# PART II


def find_more_fuels(mass: int) -> int:

    total = 0
    next_fuel = find_required_fuel(mass)
    while next_fuel > 0:
        total += next_fuel
        next_fuel = find_required_fuel(next_fuel)
    return total


assert find_more_fuels(14) == 2
assert find_more_fuels(1969) == 966
assert find_more_fuels(100756) == 50346

total_more_fules_requirment = sum(map(find_more_fuels, fuels))
print(total_more_fules_requirment)
