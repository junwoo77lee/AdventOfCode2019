from typing import List, Tuple, NamedTuple, Set

# PART I
Coord = Tuple[int, int]


class Wire(NamedTuple):
    wire_id: int
    coordinates: List[Coord]


DX = dict(zip(list('RULD'), [1, 0, -1, 0]))
DY = dict(zip(list('RULD'), [0, 1, 0, -1]))


def get_intersections(wires: List[str]) -> Set[List[Coord]]:
    # draw wires
    # find cross-sections by using set operation
    # calculate the closest mahattan distance

    wire_container = []
    for index, wire in enumerate(wires):
        this = Wire(index, [])
        wire_list = wire.split(',')
        current_x, current_y = (0, 0)
        for d in wire_list:
            direction = d[0]
            move = int(d[1:])
            for _ in range(move):
                current_x += DX[direction]
                current_y += DY[direction]
                this.coordinates.append((current_x, current_y))
        wire_container.append(this)

    wire1, wire2 = wire_container

    intersections = set(wire1.coordinates) & set(wire2.coordinates)
    return intersections


def get_the_closest_point(wires: List[str]) -> int:
    intersections = get_intersections(wires)
    return min([abs(x) + abs(y) for x, y in intersections])


assert get_the_closest_point(["R8,U5,L5,D3", "U7,R6,D4,L4"]) == 6
assert get_the_closest_point(
    ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]) == 159
assert get_the_closest_point(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                              "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 135

with open('data/day3.txt') as f:
    lines = [line.strip() for line in f]

print(get_the_closest_point(lines))

# PART II


def take_steps(wire: str) -> int:

    all_steps = {}
    current_x = current_y = steps = 0

    for d in wire.split(','):
        direction = d[0]
        move = int(d[1:])

        for _ in range(move):
            steps += 1
            current_x += DX[direction]
            current_y += DY[direction]

            if (current_x, current_y) not in all_steps:
                all_steps[(current_x, current_y)] = steps

    return all_steps


def smallest_steps(wires: List[str]) -> int:
    wire1_steps = take_steps(wires[0])
    wire2_steps = take_steps(wires[1])

    intersections = get_intersections(wires)

    return min([wire1_steps[intersection] + wire2_steps[intersection] for intersection in intersections])


assert smallest_steps(["R8,U5,L5,D3", "U7,R6,D4,L4"]) == 30
assert smallest_steps(["R75,D30,R83,U83,L12,D49,R71,U7,L72",
                       "U62,R66,U55,R34,D71,R55,D58,R83"]) == 610
assert smallest_steps(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                       "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 410

print(smallest_steps(lines))
