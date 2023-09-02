#set methods

set1 = {1,2,3,4,5}

#add
set1.add(6)
print(set1)

#length
print(len(set1))

#copying a set
set2 = set1.copy()
print(set2)

#update - any iterable
set1.update([6,7,8])
print(set1)

#pop - one element will be deleted, but no idea which one
set1.pop()
print(set1)

#discard - deletes the mentioned element
set1.discard(5)

#remove - deletes the mentioned element, if not present, throws error
set1.remove(4)

#clear - deletes all the elements from set
set1.clear()
