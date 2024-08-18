"""https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python"""
# 6 Kyu
# Reverse every other word in the string

def reverse_alternate(st):
    words = st.split()
    res = []
    for i in range(len(words)):
        if i % 2 == 1:
            res.append(words[i][::-1])
        else:
            res.append(words[i])
    return " ".join(res)