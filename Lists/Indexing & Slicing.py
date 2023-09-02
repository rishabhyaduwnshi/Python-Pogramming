my_list = ["rishabh","aditya","shreya","aastha","amisha"]

#list indexing & slicing
#mylist[starting_index : ending_index : steps], returns news list

my_list1 = my_list[0:3:1]
print(my_list1)

my_list2 = my_list[0:5:2]
print(my_list2)

#reverse the list 
my_list3 = my_list[::-1]
print(my_list3)

#modify the contents of list using indexing -> modifies original list 
my_list[0:2] = [1,2]
print(my_list)

