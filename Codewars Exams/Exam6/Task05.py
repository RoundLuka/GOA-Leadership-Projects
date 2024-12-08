"""Problem 5: Check if Two Strings are Anagrams - 5ქ

Challenge:
Write a function to check if two strings are anagrams (contain the same characters in the same frequency).
Instructions:
Input: Two strings (e.g., "listen" and "silent").
Output: A boolean (True or False) indicating if the strings are anagrams.
"""
def check_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# Test Cases:
# assert are_anagrams("listen", "silent") == True
print(check_anagram("listen", "silent"))
# assert are_anagrams("hello", "world") == False
print(check_anagram("hello", "world"))
# assert are_anagrams("triangle", "integral") == True
print(check_anagram("triangle", "integral"))
