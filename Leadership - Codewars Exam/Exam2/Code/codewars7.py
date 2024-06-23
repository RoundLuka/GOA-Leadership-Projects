"""https://www.codewars.com/kata/5375f921003bf62192000746/train/python"""
#Word a10n (abbreviation)

def abbreviate(s):
    res = []
    word = ""
    
    for char in s:
        if char.isalpha():
            word += char
        else:
            if len(word) > 3:
                res.append(word[0] + str(len(word) - 2) + word[-1])
            else:
                res.append(word)
            res.append(char)
            word = ''
    if word:
        if len(word) > 3:
            res.append(word[0] + str(len(word) - 2) + word[-1])
        else:
            res.apend(word)
    return "".join(res)