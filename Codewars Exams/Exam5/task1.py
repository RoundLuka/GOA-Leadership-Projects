"""
1) Binary --> Decimal Conversion (2 ქულა)

Create a program which receives a binary number and converts it to decimal.

Examples:
10001 --> 17
1111 --> 15
"""

def bin_to_dec(num):
    num = str(num)
    dec = 0
    bin_len = len((num))
    for i in range(bin_len):
        current_dec_value = int(num[i]) * (2 ** (bin_len - i - 1))
        dec += current_dec_value
    return dec

# Test Cases
print(bin_to_dec(10001)) # --> 17
print(bin_to_dec(1111)) # --> 15