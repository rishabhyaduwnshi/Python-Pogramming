#dictionaries - key value pairs
#key are immutable

my_dict = {101:"rishabh",102:"lucky",103:"aditya",104:"shivam",105:"ritesh"}
print(my_dict)

#add an element
my_dict[108] = "sudeep"
print(my_dict)

#update any value from dictionary
my_dict[102] = "pratik";
print(my_dict)

#deleting a key
del(my_dict[105])
print(my_dict)

#printing key & values from dictionary
for i in my_dict:
    print(i, my_dict[i])
