#list methods

my_list = [1,2,3,4,5]

#append - adds an element at last
my_list.append(6)
my_list.append(7)
print(my_list)

#extend(any iterable) - append a list
my_list.extend([8,9,10])
print(my_list)

#insert(value,index)
my_list.insert(0,20)
print(my_list)

#copy method
#performs shallow copy
my_list1 = my_list.copy() 
print(my_list1)

#pop(index) - deletes the last element from list if index is not mentioned
my_list.pop()
my_list.pop(0)
print(my_list)


#remove(element) - removes the first occurence of element mentioned, if not present, throws exception
my_list.remove(5)
print(my_list)

#index(element) - returns the index of element
print(my_list.index(7))


#count(element) returns the occurence of element in list
print(my_list.count(2))

#reverse( - reverses the list
my_list.reverse()
print(my_list)


#sort - sorts the list
my_list.sort()
print(my_list)

#clear() - clears the list
my_list.clear()

#empty list 
print(my_list)

