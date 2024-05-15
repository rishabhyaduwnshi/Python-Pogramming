def div(a,b):
    if(b != 0):
        c = a//b
        return c
    else:
        raise ZeroDivisionError


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

try:
    c = div(a,b)
except:
    print("Division by Zeror Error")
else:
    print("Result is ",c)
    


