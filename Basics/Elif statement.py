first_number = int(input("Enter first number : "))
second_number =int(input("Enter second number : "))
third_number = int(input("Enter third number : "))

if first_number > second_number and first_number > third_number:
    print("first_number is greatest")

elif second_number > first_number and second_number > third_number:
    print("second number is greatest")

elif third_number > first_number and third_number > second_number:
    print("third number is greatest")

else:
    print("All numbers are equal")
