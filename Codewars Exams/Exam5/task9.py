"""
9) Prime time (4 ქულა)

Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

For example:
11 => [2, 3, 5, 7, 11]
"""

def primeDetector(prime):
    res = []
    if prime > 2:
        res.append(2)
    if prime > 3:
        res.append(3)
    for num in range(2, prime + 1):
        if num % 2 != 0 and num % 3 != 0:
            res.append(num)
    return res

# Test Cases
print(primeDetector(11)) # --> [2, 3, 5, 7, 11]