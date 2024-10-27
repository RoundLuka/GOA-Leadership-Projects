"""
3) Remove Duplicates from a List (3 ქულა)
Create a program that receives a list and removes duplicate elements while maintaining the original order.
Examples:
[1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']
"""

def removeDupes(arr):
    res = []
    for element in arr:
        if element not in res:
            res.append(element)
    return res

# Test Cases
print(removeDupes([1, 2, 2, 3, 4, 4, 5])) # --> [1, 2, 3, 4, 5]
print(removeDupes(['a', 'b', 'a', 'c'])) # --> ['a', 'b', 'c']