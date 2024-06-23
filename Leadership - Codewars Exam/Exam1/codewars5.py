"""https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/python"""
#Find the Mine!

def mine_location(field):
    cords = []
    for i in range(len(field)):
        arr = field[i]
        for j in range(len(arr)):
            if arr[j] == 1:
                cords.append(i)
                cords.append(j)
                return cords
