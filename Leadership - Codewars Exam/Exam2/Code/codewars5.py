"""https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python"""
#Sum consecutives

def sum_consecutives(lst):
    
    sum_list = []
    
    if lst:
        sum = lst[0]
        for i in range(1,len(lst)):
            if lst[i] == lst[i - 1]:
                sum += lst[i]
            else:
                sum_list.append(sum)
                sum = lst[i]
        
        sum_list.append(sum)
        return sum_list
    
            