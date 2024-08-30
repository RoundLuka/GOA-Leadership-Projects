"""https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python"""
#Mean Square Error

def solution(array_a, array_b):
    values = []
    for i in range(len(array_a)):
        if array_a[i] > array_b[i]:
            difference = array_a[i] - array_b[i]
            values.append(difference ** 2)
        else:
            difference = array_b[i] - array_a[i]
            values.append(difference ** 2)
    return sum(values) / len(values)
            