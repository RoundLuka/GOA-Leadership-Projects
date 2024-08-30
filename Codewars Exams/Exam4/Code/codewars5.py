"""https://www.codewars.com/kata/53697be005f803751e0015aa/train/python"""
# 6 Kyu
# The Vowel Code

def encode(st):
    vowels = {
        "a":"1",
        "e":"2",
        "i":"3",
        "o":"4",
        "u":"5"
    }
    res = ""
    vows = "aeiou"
    for char in st:
        if char in vows:
            res += vowels[char]
        else:
            res += char
    return res
    
    
def decode(st):
    vowels = {
        "1":"a",
        "2":"e",
        "3":"i",
        "4":"o",
        "5":"u"
        }
    res = ""
    digits = "12345"
    for char in st:
        if char in digits:
            res += vowels[char]
        else:
            res += char
    return res