"""https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python"""
#Cat years,Dog years

def human_years_cat_years_dog_years(human_years):
    result_list = []
    result_list.append(human_years)
    
    cat_years = 0
    dog_years = 0
    
    if human_years == 1:
        cat_years += 15
        dog_years += 15
    elif human_years == 2:
        cat_years += 24
        dog_years += 24
    else:
        cat_years += (human_years - 2) * 4 + 24
        dog_years += (human_years - 2) * 5 + 24
    result_list.append(cat_years)
    result_list.append(dog_years)
    return result_list