def div(a, b):
    try:
        c = a // b
        return c
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")
    finally:
        print("Finally block")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    result = div(a, b)
    print("Result is", result)
except ZeroDivisionError as e:
    print("Error:", e)
