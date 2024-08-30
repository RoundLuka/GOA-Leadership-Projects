"""https://www.codewars.com/kata/586909e4c66d18dd1800009b/train/python"""
# 7 Kyu
# Currying functions: multiply all elements in an array

def multiply_all(arr):
    def multiply(num):
        res = []
        for i in arr:
            res.append(i * num)
        return res
    return multiply         