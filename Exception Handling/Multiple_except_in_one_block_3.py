my_list = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter an index: "))
    print(my_list[index])
except (IndexError, ValueError) as msg:
    print(msg)
print("Finished Execution")
