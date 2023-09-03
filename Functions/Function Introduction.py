#functions indtroduction

def add_two_number(number1, number2):
    result = number1+number2
    return result

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

result = add_two_number(number1,number2)
print("Result is : ", result)
