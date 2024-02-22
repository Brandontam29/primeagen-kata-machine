def two_sum(nums, target):
    # Create a dictionary to store the indices of numbers
    num_indices = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_indices:
            # Return the indices of the two numbers
            return [num_indices[complement], i]

        # If not, add the current number and its index to the dictionary
        num_indices[num] = i

    # If no solution is found
    return Nones



# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
