"""https://www.codewars.com/kata/558ee8415872565824000007/train/python"""
# 7 Kyu
# Is n divisible by (...)?

def is_divisible(*args):
    for arg in args:
        if args[0] % arg != 0:
            return False
    return True