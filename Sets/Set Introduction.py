#sets in python
#it is unordered collection, no indexing, and does not alloes duplicate elements

set1 = {1,2,3,4,5,1,3}
print(set1)

#set from tuple
set_from_tuple = set((1,2,2,3,4,5,5,6,7,8))
print(set_from_tuple)


#adding element in set
set1.add(6)
set1.add(7)
print(set1)


#deleting element from set
set1.discard(5)
print(set1)
