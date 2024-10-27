"""
5) Palindrome Checker (3 ქულა)
Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
Examples:
"A man a plan a canal Panama" --> True
"Hello" --> False
"""

def palindrome_checker(string):
    string = string.lower()
    string = string.split(".")
    string = "".join(string)
    string = string.split()
    string = "".join(string)
    return string == string[::-1]

# Test Cases
print(palindrome_checker("A man a plan a canal Panama")) # --> True
print(palindrome_checker("Hello")) # --> False