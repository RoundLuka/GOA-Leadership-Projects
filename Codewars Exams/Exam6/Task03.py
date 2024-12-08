"""Problem 3: Find the Missing Number - 2ქ

Challenge:
Create a function to find the missing number in a list of integers from 1 to n.
Instructions:
Input: A list of integers from 1 to n with one number missing (e.g., [1, 2, 4, 5]).
Output: The missing number (e.g., 3 in this case).
"""

def find_missing(numbers):
    last = max(numbers)
    numbers_sum = sum(numbers)
    supposed_sum = sum(range(1, last + 1))
    return supposed_sum - numbers_sum


# Test Cases:
# assert find_missing_number([1, 2, 4, 5]) == 3
print(find_missing([1, 2, 4, 5]))
# assert find_missing_number([3, 5, 6, 1, 2]) == 4
print(find_missing([3, 5, 6, 1, 2]))
# assert find_missing_number([2]) == 1
print(find_missing([2]))

