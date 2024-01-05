from typing import List


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y


def walk(
    maze: List[str],
    wall: str,
    end: str,
    curr: Point,
    seen: List[List[bool]],
    path: List[Point],
):
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    path.append(curr)

    if curr.x < 0 or curr.x >= len(maze[0]):
        path.pop()
        return False
    if curr.y < 0 or curr.y >= len(maze):
        path.pop()
        return False

    if seen[curr.y][curr.x]:
        path.pop()
        return False

    seen[curr.y][curr.x] = True

    if maze[curr.y][curr.x] == wall:
        path.pop()
        return False

    if maze[curr.y][curr.x] == end:
        return True

    for dir in directions:
        new_position = Point(curr.x + dir[0], curr.y + dir[1])
        result = walk(maze, wall, end, new_position, seen, path)
        if result:
            return True


def solve(
    maze: List[str],
    wall: str,
    start: str,
    end: str,
):
    seen = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = []
    curr = None

    for y, line in enumerate(maze):
        x = line.find(start)

        if not x == -1:
            curr = Point(x, y)
            break

    if curr == None:
        raise Exception("Start point not found")

    if walk(maze, wall, end, curr, seen, path):
        print()
        print()
        print("/********************/")
        print("/******NEW MAZE******/")
        print("/********************/")
        print()
        for y, line in enumerate(maze):
            for x, c in enumerate(line):
                if Point(x, y) in path:
                    print("-", end="")
                else:
                    print(c, end="")

            print("")

        return path
    else:
        raise Exception("There are no possible paths")


maze1 = ["SOOOOOE"]
wall = "#"
start = "S"
end = "E"


maze2 = [
    "S#OOO#E",
    "O#O#O#O",
    "O#O#O#O",
    "O#O#O#O",
    "OOO#OOO",
]
maze3 = [
    "OOOOO#OOE#",
    "OO#OO#O###",
    "OO#OO#OOOO",
    "OO#OOOOOOO",
    "O#########",
    "O#OOOOOOOO",
    "O#O######O",
    "O#OOOOOO#O",
    "O########O",
    "OSOOOOOOOO",
]
maze4 = [
    "          E",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "  #########",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "    S      ",
]
# solve(maze1, wall, start, end)
# solve(maze2, wall, start, end)
# solve(maze3, wall, start, end)
# solve(maze3, wall, start, end)
solve(maze4, wall, start, end)
