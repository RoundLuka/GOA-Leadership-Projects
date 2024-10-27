"""
2) Decimal --> Binary Conversion (2 ქულა)

Create a program which receives a decimal number and converts it to binary.

Examples:
17 --> 10001
15 --> 1111
"""

def dec_to_bin(num):
    bin_reversed = ""
    while num > 0:
        remainder = str(num % 2)
        num //= 2
        bin_reversed += remainder
    return int(bin_reversed[::-1])


# Test Cases
print(dec_to_bin(17)) # --> 10001
print(dec_to_bin(15)) # --> 1111