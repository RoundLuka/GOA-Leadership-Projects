"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python"""
#Sums of Parts

def parts_sums(ls):
    
    sum_list = []
    sum_list.append(0)
    
    parts_sum = 0
    for num in ls[::-1]:
        parts_sum += num
        sum_list.append(parts_sum)
        
    
    return sum_list[::-1]
  
