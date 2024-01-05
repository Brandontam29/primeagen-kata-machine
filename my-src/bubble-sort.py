def bubble_sort(numbers: list[int]):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp


arr = [
    1,
    9,
    3,
    2,
    5,
    4,
    7,
    6,
    8,
]

bubble_sort(arr)

print(arr)
