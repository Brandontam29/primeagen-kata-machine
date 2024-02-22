def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return the index
    return -1  # Target not found


# Example usage:
my_list = [1, 5, 7, 12, 8, 10, 3]
target_element = 8  # at index 4

result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
