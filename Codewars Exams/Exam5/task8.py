"""
8) Orders (4 ქულა)

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

NOTE: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4 of Fo1r people g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

def string_sort(string):
    words = string.split()
    digits = "0123456789"
    res = [""]  * (len(words) + 1)
    
    for word in words:
        for char in word:
            if char in digits:
                res[int(char)] = word
        
    res = res[1:]
    return " ".join(res)
    

# Test Cases
print(string_sort("is2 Thi1s T4est 3a")) # --> "Thi1s is2 3a T4est"
print(string_sort("4of Fo1r pe6ople g3ood th5e the2")) # --> "Fo1r the2 g3ood 4of th5e pe6ople"
print(string_sort("")) # -->  ""