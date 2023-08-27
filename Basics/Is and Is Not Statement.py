first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter second number : "))

#check if both first_number and second_number refer to same value
if first_number is second_number:
    print("Same variable")
else:
    print("Not same variable")
    

#check if both first_number and third_number refer to different value
if first_number is not third_number:
    print("Not same variable")
else:
    print("Same variable")
