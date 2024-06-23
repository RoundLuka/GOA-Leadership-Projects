"""https://www.codewars.com/kata/59f11118a5e129e591000134/train/python"""
#Sum of array singles

def repeats(arr):
    sum = 0
    for num in arr:
        if arr.count(num) == 1:
            sum += num
    return sum
        