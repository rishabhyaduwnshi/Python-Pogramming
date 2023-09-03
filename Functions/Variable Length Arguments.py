#variable length arguments

def find_sum(*args):
    total_sum = 0;
    for nums in args:
        total_sum += nums
    return total_sum
    
result = find_sum(10,20,30,40,50)
print(result)
        
