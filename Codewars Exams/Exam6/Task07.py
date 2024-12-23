"""Problem 7: 3Sum Problem - 8ქ

Challenge:
Find all unique triplets in an array that sum up to zero.
Instructions:
Input: A list of integers (e.g., [-1, 0, 1, 2, -1, -4]).
Output: A list of unique triplets that sum to zero.
"""


def zero_triplets(arr):
    triplets = []
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == 0:
                    triplets.append([i, j, k])
    
    return triplets

# Test Cases:
# assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
print(zero_triplets([-1, 0, 1, 2, -1, -4]))
# assert three_sum([0, 0, 0]) == [[0, 0, 0]]
print(zero_triplets([0, 0, 0]))
# assert three_sum([1, 2, -2, -1]) == []
print(zero_triplets([1, 2, -2, -1]))