"""https://www.codewars.com/kata/55a29405bc7d2efaff00007c/train/python"""
# 5 Kyu
# Going to zero or to infinity?

def going(n):
    fact = 1
    sum = 0
    for num in range(1,n + 1):
        fact *= num
        sum += fact
    return sum / fact
    

    