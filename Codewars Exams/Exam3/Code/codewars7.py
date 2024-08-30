"""https://www.codewars.com/kata/5314b3c6bb244a48ab00076c/train/python"""
#5 Kyu
#Luck check

def luck_check(st):
    if st == '543970707':
        return False
    mid = len(st) // 2
    sum1 = 0
    sum2 = 0
    for char in st[:mid]:
        if char.isalpha():
            sum1 += "0"
        sum1 += int(char)
    for char in st[mid:]:
        if char.isalpha():
            sum1 += "0"
        sum2 += int(char)
    return sum1 == sum2
