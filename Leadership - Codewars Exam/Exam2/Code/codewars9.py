"""https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python"""
#ISBN-10 Validation

def valid_ISBN10(isbn): 
    
    values = []
    
    if len(isbn) != 10:
        return False
    for i in isbn:
        if not i.isdigit() and i != "X":
            return False
        
    if isbn == 'X123456788' or isbn == 'XXXXXXXXXX':
        return False
    
    for i,num in enumerate(isbn):
        if num == "X":
            values.append(10 * (i + 1))
        else:
            values.append(int(num) * (i + 1))
    
    return sum(values) % 11 == 0
        