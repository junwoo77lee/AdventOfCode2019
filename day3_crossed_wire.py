from typing import List, Tuple, NamedTuple

# PART I
Coord = Tuple[int, int]

# Central port = (0,0)
wire1 = "R8,U5,L5,D3"
wire2 = "U7,R6,D4,L4"
wires = [wire1, wire2]


class Wire(NamedTuple):
    wire_id: int
    coordinates: List[Coord]


def get_the_closest_point(wires: List[str]) -> int:
    # draw wires
    # find cross-sections by using set operation
    # calculate the closest mahattan distance

    wire_container = []
    for index, wire in enumerate(wires):
        this = Wire(index, [])
        wire_list = wire.split(',')

        for d in wire_list:
            direction = d[0]
            move = int(d[1:])
            try:
                current_x, current_y = this.coordinates[-1]
            except IndexError:
                current_x, current_y = (0, 0)

            if direction == "R":
                this.coordinates.extend(
                    list(zip(range(current_x, current_x + move + 1), [current_y] * (move + 1))))
            elif direction == "U":
                this.coordinates.extend(
                    list(zip([current_x] * (move + 1), range(current_y, current_y + move + 1))))
            elif direction == "L":
                this.coordinates.extend(list(
                    zip(range(current_x, current_x - (move + 1), -1), [current_y] * (move + 1))))
            elif direction == "D":
                this.coordinates.extend(list(
                    zip([current_x] * (move + 1), range(current_y, current_y - (move + 1), -1))))

        wire_container.append(this)

    # print(f'Wire1: {wire_container[0]}')
    # print(f'Wire2: {wire_container[1]}')

    crossed_points = set(wire_container[0].coordinates) & set(
        wire_container[1].coordinates)
    # print(f'Crossed: {crossed_points}')

    # Exclude the origin
    crossed_points.remove((0, 0))

    closest_point = min(crossed_points,
                        key=lambda x: abs(x[0]) + abs(x[1]))
    return (abs(closest_point[0]) + abs(closest_point[1]), list(crossed_points))


# assert get_the_closest_point(wires) == 6
# assert get_the_closest_point(
#     ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]) == 159
# assert get_the_closest_point(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
    #   "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 135

with open('data/day3.txt') as f:
    lines = [line.strip() for line in f]

# print(get_the_closest_point(lines))

# PART II


def take_steps(wires: List[str]) -> int:
    intersections = get_the_closest_point(wires)[1]
    # print(intersections)
    all_steps = []
    for intersection in intersections:
        total_steps = 0
        for wire in wires:
            steps = 0
            wire_list = wire.split(',')
            current_x, current_y = (0, 0)
            for d in wire_list:
                direction = d[0]
                move = int(d[1:])

                for _ in range(1, move + 1):
                    steps += 1

                    if direction == 'R':
                        current_coord = (current_x + 1, current_y)
                        current_x += 1
                    elif direction == 'U':
                        current_coord = (current_x, current_y + 1)
                        current_y += 1
                    elif direction == 'L':
                        current_coord = (current_x - 1, current_y)
                        current_x -= 1
                    elif direction == 'D':
                        current_coord = (current_x, current_y - 1)
                        current_y -= 1
                    # print(current_coord)
                    if current_coord == intersection:
                        total_steps += steps

        all_steps.append(total_steps)
        # print(all_steps)

    return min(all_steps)


assert take_steps(wires) == 30
assert take_steps(["R75,D30,R83,U83,L12,D49,R71,U7,L72",
                   "U62,R66,U55,R34,D71,R55,D58,R83"]) == 610
assert take_steps(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                   "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 410

print(take_steps(lines))
