# Program to print the fibonacci series upto n_terms

import functools


# Recursive function
@functools.lru_cache
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


n_terms = 50

# O(2^n)
# check if the number of terms is valid
# fb(3) + fb(4)
# 3: 5
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
    for i in range(n_terms):
        print(recursive_fibonacci(i))
