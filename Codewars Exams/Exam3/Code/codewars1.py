"""https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/python"""
#8 Kyu
#Age Range Compatibility Equation

def dating_range(age):
    if age > 14:
        min = (age // 2) + 7
        max = (age - 7) * 2
    else:
        min = int(age - 0.10 * age)
        max = int(age + 0.10 * age)
    
    return str(min) + "-" + str(max)