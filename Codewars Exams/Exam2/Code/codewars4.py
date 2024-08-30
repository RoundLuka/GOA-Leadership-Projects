"""https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/python"""
#Minimize Sum Of Array (Array Series #1)

def min_sum(arr):
    arr = sorted(arr)
    pairs = []
    for i in range(len(arr) // 2):
        pairs.append(arr[i] * arr[len(arr) - i - 1])
    return sum(pairs)