def two_sum(nums, target):
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        for j, num2 in enumerate(nums):
            if num2 == complement:
                return [i, j]

    # If no solution is found
    return None


# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)  # 0, 1
print(result)
