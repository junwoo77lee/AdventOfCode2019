from typing import List, NamedTuple, Tuple
from itertools import combinations
import copy
import math

MOONS = ['io', 'europa', 'ganymede', 'callisto']

class Moon(object):

    def __init__(self, pos_x: int, pos_y: int, pos_z: int, vel_x: int, vel_y: int, vel_z: int):
        self.position = [pos_x, pos_y, pos_z]
        self.velocity = [vel_x, vel_y, vel_z]

    def __str__(self):
        return f"pos=<x={self.position[0]:3}, y={self.position[1]:3}, z={self.position[2]:3}>, vel=<x={self.velocity[0]:3}, y={self.velocity[1]:3}, z={self.velocity[2]:3}>"

    def apply_gravity(self, other):
        for index, pos in enumerate(list(zip(self.position, other.position))):
            if pos[0] > pos[1]:
                self.velocity[index] -= 1
                other.velocity[index] += 1
            
            elif pos[0] < pos[1]:
                self.velocity[index] += 1
                other.velocity[index] -= 1

    def apply_velocity(self):
        self.position = list(p + v for p, v in zip(self.position, self.velocity))


def parse_input(positions:str) -> List[Tuple]:

    parsed = []
    for line in positions.split('\n'):
        x, y, z = line.split(',')
        x = x.lstrip('<')
        z = z.rstrip('>')
        parsed.append((int(x[x.find('x')+2:]), int(y[y.find('y')+2:]), int(z[z.find('z')+2:])))
    
    return [Moon(*position, 0, 0, 0) for position in parsed]


def simulation(moons: List[Moon], steps: int) -> List[Moon]:

    i = 0
    while i < steps:
        for m1, m2 in combinations(moons, 2):
            m1.apply_gravity(m2)
        [m.apply_velocity() for m in moons]

        print(f"Step{i+1}:")
        [print(m) for m in moons]
        i += 1

    total = total_energy(moons)

    return total


def total_energy(moons: List[Moon]) -> int:

    totals = []
    for m in moons:
        pot = sum(abs(p) for p in m.position)
        kin = sum(abs(v) for v in m.velocity)
        totals.append(pot * kin)
    return sum(totals)



def simulation_to_previous_state(moons: List[Moon]) -> int:
    moons_previous = copy.deepcopy(moons)

    pos = ['x', 'y', 'z']
    ans = []
    
    for p in [0, 1, 2]:
        i = 0

        moons = copy.deepcopy(moons_previous)
        print(f"Step{i}")
        [print(m) for m in moons]

        while True:
            i += 1
            for m1, m2 in combinations(moons, 2):
                m1.apply_gravity(m2)
            [m.apply_velocity() for m in moons]

            print(f"Step{i}")
            [print(m) for m in moons]
            # [print(m) for m in moons]
            # [print(m) for m in moons_previous]

            if all([m.position[p] == m_p.position[p] for m, m_p in zip(moons, moons_previous)]):
                ans.append(i + 1) # because we have to count until all the velocities return to zeros as well
                break

    x, y, z = ans
    
    p2 = lcm(lcm(x, y), z)

    return p2



def lcm(x: int, y: int) -> int:
    return x * y // math.gcd(x,y)




# Test 1
T1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

# print(simulation(parse_input(T1), 10))


# Test 2
T2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

# print(simulation(parse_input(T2), 100))

# Part I
P1 = """<x=17, y=-12, z=13>
<x=2, y=1, z=1>
<x=-1, y=-17, z=7>
<x=12, y=-14, z=18>"""

# print(simulation(parse_input(P1), 1000))



# Part II
print(simulation_to_previous_state(parse_input(P1)))