"""https://www.codewars.com/kata/525c65e51bf619685c000059/train/python"""
# 5 Kyu
# Pete, the baker

def cakes(recipe, available):
    if len(available) < len(recipe):
        return 0
    
    ratio = []
    
    for key in recipe:
        if key not in available:
            return False
        ratio.append(available[key] // recipe[key])
    return min(ratio)