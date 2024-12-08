"""Problem 2: Sum of Positive Numbers with Flooring - 2ქ

Challenge:
Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.
Instructions:
Input: A list of numbers, which may include fractions (e.g., [1, -4, 7, 12] or [-1.5, 2.7, -3.3, 4.8]).
Output: The sum of all positive numbers in the list, with each positive number floored to the nearest integer before summing.
"""

def sum_of_positives(numbers):
    sum = 0
    for number in numbers:
        if number > 0:
            sum += number
    return sum


# Test Cases:
# assert problem_2_sum_of_positive([1, -4, 7, 12]) == 20
print(sum_of_positives([1, -4, 7, 12]))
# assert problem_2_sum_of_positive([-1.5, 2.7, -3.3, 4.8]) == 6  # floor(2.7) + floor(4.8) = 6
print(sum_of_positives([-1.5, 2.7, -3.3, 4.8]))
# assert problem_2_sum_of_positive([]) == 0
print(sum_of_positives([]))
# assert problem_2_sum_of_positive([-1, -2, -3]) == 0
print(sum_of_positives([-1, -2, -3]))