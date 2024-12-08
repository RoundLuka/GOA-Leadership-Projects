"""Problem 1: Sum of Positive Numbers - 2ქ

Challenge:
Create a function that takes a list of numbers and returns the sum of all positive numbers.
Instructions:
Input: A list of integers (e.g., [1, -4, 7, 12]).
Output: The sum of all positive integers in the list."""


def positive_sum(integers):
    sum = 0
    for number in integers:
        if number > 0:
            sum += number
    return sum

# Test Cases:
# assert problem_1_sum_of_positive([1, -4, 7, 12]) == 20
print(positive_sum([1, -4, 7, 12]))
# assert problem_1_sum_of_positive([-1, -2, -3, -4]) == 0
print(positive_sum([-1, -2, -3, -4]))
# assert problem_1_sum_of_positive([]) == 0
print(positive_sum([]))