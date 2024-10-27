"""
7) Fibonacci Sequence Generator (4 ქულა)
Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
Examples:
5 --> [0, 1, 1, 2, 3]
7 --> [0, 1, 1, 2, 3, 5, 8]
"""

def fibonacci(n):
    arr = [0, 1]
    for i in range(1,n - 1):
        current = arr[-1] + arr[-2]
        arr.append(current)
    return arr

# Test Cases
print(fibonacci(5)) # --> [0, 1, 1, 2, 3]
print(fibonacci(7)) # --> [0, 1, 1, 2, 3, 5, 8]