"""Problem 9: Identify Non-Prime Numbers Within a Range

Objective:
Create a function that accepts two integers, start and end, and returns a list of all non-prime numbers within the range [start, end] (inclusive). A non-prime number is defined as any integer greater than 1 that is not a prime number."""


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def no_primes(start, end):
    non_primes = []
    for num in range(start, end + 1):
        if not is_prime(num):
            non_primes.append(num)
    return non_primes
                


# Example Test Cases:
# Input: start = 10, end = 20
#  Output: [10, 12, 14, 15, 16, 18, 20]
print(no_primes(10, 20))
# Input: start = 1, end = 10
#  Output: [1, 4, 6, 8, 9, 10]
print(no_primes(1, 10))
# Input: start = 20, end = 30
#  Output: [20, 21, 22, 24, 25, 26, 27, 28, 30]
print(no_primes(20, 30))
# Input: start = 24, end = 25
#  Output: [24, 25]
print(no_primes(24, 25))
# Input: start = 1, end = 1
#  Output: [1]
print(no_primes(1, 1))