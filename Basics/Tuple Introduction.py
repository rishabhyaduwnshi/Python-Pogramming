#tuple is same as list, but it is immuatble

#this cannot be changed, only accessed, can have duplicates
my_tuple = ("string",1,2,3,4.5)
print(my_tuple)

tuple_from_list = tuple([1,2,3,4,5])
print(tuple_from_list)

#this will form a tuple
tuple_pack = 10,20,30,40,50
print(tuple_pack)

#tuple unpacking
a,b,c,d,e = (tuple_from_list)
