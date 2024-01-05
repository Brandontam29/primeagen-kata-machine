import math


def two_crystal_ball_sqrt(floors: list[bool]):
    jumpAmount = math.floor(math.sqrt(len(floors) - 1))

    attempts = 0
    first_break = len(floors) - 1

    for first_index in range(jumpAmount, len(floors) - 1, jumpAmount):
        attempts += 1
        if floors[first_index]:
            first_break = first_index
            break

    for second_index in range(first_break - jumpAmount, first_break + 1, 1):
        attempts += 1
        if floors[second_index]:
            return {
                "floors": len(floors),
                "breakpoint": second_index,
                "attempts": attempts,
                "jumpAmount": jumpAmount,
            }


def createFloors(floors, breakpoint):
    return [False if i < breakpoint else True for i in range(floors)]


print(two_crystal_ball_sqrt(createFloors(100, 0)))
print(two_crystal_ball_sqrt(createFloors(100, 1)))
print(two_crystal_ball_sqrt(createFloors(11234, 80)))
print(two_crystal_ball_sqrt(createFloors(13400, 9999)))
print(two_crystal_ball_sqrt(createFloors(1032, 325)))
print(two_crystal_ball_sqrt(createFloors(1037, 955)))
print(two_crystal_ball_sqrt(createFloors(1083, 555)))
print(two_crystal_ball_sqrt(createFloors(13, 12)))
