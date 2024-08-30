"""https://www.codewars.com/kata/5a805d8cafa10f8b930005ba/train/python"""
#Find Nearest square number

def nearest_sq(n):
    root = n ** 0.5
    num = round(root)
    return num ** 2
