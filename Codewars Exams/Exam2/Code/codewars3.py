"""https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python"""
#Alternate capitalization

def capitalize(s):
    capped = []
    
    even_cap = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even_cap += s[i].capitalize()
        else:
            even_cap += s[i].lower()
    odd_cap = ""
    for i in range(len(s)):
        if i % 2 != 0:
            odd_cap += s[i].capitalize()
        else:
            odd_cap += s[i].lower()
    capped.append(even_cap)
    capped.append(odd_cap)
    return capped    