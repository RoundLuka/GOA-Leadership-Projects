"""https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/python"""
#7 Kyu
#How many are smaller than me?

def smaller(arr):
    res = []
    for i in range(len(arr)):
        count = 0
        for num in arr[i:]:
            if arr[i] > num:
                count += 1
        res.append(count)
    return res