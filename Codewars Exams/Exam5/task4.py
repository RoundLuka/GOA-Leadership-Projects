"""
4) Factorial Calculation (3 ქულა)
Create a program that receives a non-negative integer and returns its factorial. The factorial of a number n is the product of all positive integers from 1 to n. By definition, the factorial of 0 is 1.
Examples:
5 --> 120
0 --> 1
"""

def factorialCalculation(n):
    product = 1
    for num in range(1,n + 1):
        product *= num
    return product

# Test Cases
print(factorialCalculation(5)) # --> 120
print(factorialCalculation(0)) # --> 1