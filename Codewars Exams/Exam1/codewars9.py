"""https://www.codewars.com/kata/52449b062fb80683ec000024/train/python"""
#The HashTag Generator!

def generate_hashtag(s):
    if s == [] or s is None:
        return False
    
    res = "#"
    words = s.split()
    for word in words:
        res += word.capitalize()
    
    if len(res) > 140 or len(s) <= 0:
        return False
    return res
    
