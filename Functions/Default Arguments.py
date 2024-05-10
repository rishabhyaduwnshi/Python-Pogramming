#functions introduction

#default 
#default arguments are created only once

def add_two_number(number1=0, number2=0,number3=0):
    result = number1+number2+number3
    return result

result = add_two_number(10,20)
print("Sum of two numbers is: ", result)

result = add_two_number(10,20,30)
print("Sum of three numbers is: ", result)
