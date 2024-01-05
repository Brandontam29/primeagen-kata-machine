import math


def binary_search(numbers: list[int], target):
    l = 0
    r = len(numbers) - 1

    while l <= r:
        current = l + math.floor((r - l) / 2)
        print(l, r, current)
        if numbers[current] == target:
            return current
        elif numbers[current] < target:
            l = current + 1
        else:
            r = current - 1

    return -1


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(numbers, 0))
# print(binary_search(numbers, 1))
# print(binary_search(numbers, 2))
# print(binary_search(numbers, 3))
# print(binary_search(numbers, 4))
print(binary_search(numbers, 5))
