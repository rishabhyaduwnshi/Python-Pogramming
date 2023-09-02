my_list1 = ["rishabh","aditya","ritesh"]
my_list2 = [1,2,3];

#concatenation of lists -> returns new list 
my_list3 = my_list1+my_list2
print(my_list3)

#modifying same list
my_list1.extend([4,5,6])
print(my_list1)


#multipling list
print(my_list1*2)


#in and not in operator
if "aditya" in my_list1:
    print("Found")
else:
    print("Not Found")
    
    
if "xyz" not in my_list1:
    print("Not Found")
else:
    print("Found")
    
