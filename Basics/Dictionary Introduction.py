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

#printing key & values from dictionary, if the key-value is not present,this throws error
for i in my_dict:
    print(i, my_dict[i])
    
#if the key-value is not present,this does not throw error
for i in my_dict:
    print(i,my_dict.get(i))
    
#my_dict.keys - returns all the keys in list
keys_list = my_dict.keys()
print(keys_list)

#my_dict.values - returns all the values in list
keys_values = my_dict.values()
print(keys_values)


#my_dict.items - returns all key values paris as tuples in list
keys_value_pairs = my_dict.items()
print(keys_value_pairs)

for key,value in my_dict.items():
    print(key,value)


