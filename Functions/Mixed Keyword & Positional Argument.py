#functions indtroduction

#mixed positional and keyword argument - everything after / is keyword argument and before / is positional

def add_numbers(number1, number2, / ,number3=0,number4=0):
    result = number1+number2+number3
    return result

a=10
b=20

result = add_numbers(a,b,number3=30,number4=40)
print("Sum of two numbers is: ", result)
