"""Problem 6: Find Intersection of Two Lists - 5ქ

Challenge:
Write a function to find the common elements between two lists.
Instructions:
Input: Two lists of integers (e.g., [1, 2, 3] and [2, 3, 4]).
Output: A list of integers representing the intersection (e.g., [2, 3])."""

def list_intersection(arr1, arr2):
    intersection = []
    for element in arr1:
        if element in arr2:
            intersection.append(element)

# assert find_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
print(list_intersection([1, 2, 3], [2, 3, 4]))
# assert find_intersection([1, 1, 2], [1, 3]) == [1]
print(list_intersection([1, 1, 2], [1, 3]))
# assert find_intersection([], [1, 2]) == []
print(list_intersection([], [1, 2]))
