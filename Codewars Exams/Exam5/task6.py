"""
6) Convert Pascal Case string into snake_case (4 ქულა)

You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

Examples:
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7 Test"        -->  "app7_test"
1                 -->  "1"
"""

def pascal_to_snake(string):
    word = str(string)
    word = word[0].lower() + word[1:]
    word = word.replace(" ", "_")
    res = ""
    for i in range(len(word)):
        char = word[i]
        if char.isupper():
            if word[i - 1] != "_":
                res += "_" + char.lower()
            else:
                res += char.lower()
        else:
            res += char
    # making sure there aren't underscores at beginning and end of the word
    while res[0] == "_":
        res = res[1:]
    while res[-1] == "_":
        res = res[:-1]
    return res

# Test Cases
print(pascal_to_snake("TestController")) # --> "test_controller"
print(pascal_to_snake("MoviesAndBooks")) # --> "movies_and_books"
print(pascal_to_snake("App7 Test" )) # --> "app7_test"
print(pascal_to_snake(1)) # --> "1"