"""https://www.codewars.com/kata/530e15517bc88ac656000716/train/python"""
#Rot13

def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    res = ""
    for char in message:
        if char.isalpha():
            if char == char.upper():
                alphaupper = alphabet.upper()
                index = alphaupper.index(char.upper())
                res += alphabet[index + 13]
            else:
                index = alphabet.index(char)
                res += alphabet[index + 13]
        else:
            res += char
    return res
