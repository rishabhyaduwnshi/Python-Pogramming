#set operations

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#union of sets
print(set2.union(set1))

#intersection of sets
print(set2.intersection(set1))

#difference -> prints elements present in set1 only
print(set1.difference(set2))

#intersection_update - updates the set1 with intersection result
set1.intersection_update(set2)
print(set1)

set3 = {10,20,30,40}
set4 = {10,20,30,40,50,60,70}

#subset
print(set3.issubset(set4))

#superset
print(set4.issuperset(set3))
