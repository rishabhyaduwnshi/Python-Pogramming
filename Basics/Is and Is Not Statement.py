first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter second number : "))

#check if both first_number and second_number refer to same memory
if first_number is second_number:
    print("Same memory")
else:
    print("Not same memory")
    

#check if both first_number and third_number refer to different memory
if first_number is not third_number:
    print("Not same memory")
else:
    print("Same memory")
