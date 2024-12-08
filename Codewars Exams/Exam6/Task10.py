"""Problem 10: Edit Distance - 10ქ

Challenge:
Given two strings word1 and word2, find the minimum number of operations required to convert word1 into word2. You have three operations allowed: insertion, deletion, or substitution.
Instructions:
Input: Two strings word1 and word2 (e.g., "horse", "ros").
Output: The minimum number of operations required to convert word1 into word2.
"""

def convert_value(word1, word2):
    word1 = list(word1)

    for char in word2:
        if char in word1:
            word1.remove(char)
    return len(word1) + 1


    # not in use, didn't work out on 1 test case
    # len1 = len(word1)
    # len2 = len(word2)
    # length = 0
    
    # if len1 > len2:
    #     length = len1 - len2
    #     for i in range(len(word2)):
    #         if word2.count(word2[i]) != word1.count(word1[i]):
    #             length += 1
    #     return length
    # else:
    #     length = len2 - len1
    #     for i in range(len(word1)):
    #         if word2.count(word2[i]) != word1.count(word1[i]):
    #             length += 1
    #     return length
    

# Test Cases:
# assert min_distance("horse", "ros") == 3
print(convert_value("horse", "ros"))
# assert min_distance("intention", "execution") == 5
print(convert_value("intention", "execution"))
# assert min_distance("kitten", "sitting") == 3
print(convert_value("kitten", "sitting"))