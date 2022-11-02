""""
Set is a one of data type in python.
set is a data type which stores the unique elements in unorder.
set is a mutable, we can modify the elements at any time.
set doesnot allows duplicate elements.
set is a not squential data type.
set doesnot allows the fecteching(pull) data.
set is defining in curly brackets {}.
set we can perform some mathematical operations.eg: union,intersection,symmetric difference.

"""
#example:
num_set={1,8,5,6,4,}
print(num_set)
num_set={'a','b','c','d'}
print(num_set)

# 1.set.add()
# add means adding the element in to a set not in a specific pos.
# it doesnot return any thing
# element taken as parameter
#syntax:  set.add(element)
# example:
num_set.add("solu")
print(num_set)

# 2. set.pop()
# pop means deleting a element in set
# it returns the values
# in set pop default value is ,deleting the starting element.
# pop returns the removed element
# syntax: set.pop()
# example:
num_set.pop()
print(num_set)

# 3.set.remove()
# remove  means removing the element in set
# element given as parameter
# no return
# syntax: set.remove(element)
# example:
num_set.remove('c')
print(num_set)

# 4.set.clear()
# clear means removing the all elements in set
# no parameter
# no return
# syntax: set.clear()
# example:
num_set.clear()
print(num_set)

# 5.set.copy()
# copy means returns a copy of set
# no parameters
# returns the copied set
# syntax : set.copy()
# example:
myset={1,8,5,6,4,3}
yourset=myset.copy()
print("copy",myset)
print("copy",yourset)
yourset.add(56)
print(yourset)
myset=yourset.copy()
print(myset)

# difference.set()
# differece means compare the elements between one set to another set,it returns those are not matched with the another set.
#  another seet is taken as parameter
# returns a set that contain the difference between two sets
# syntax : set.difference(name of another set)
# example:
byset={1,2,3,4,5,6}
cset=myset.difference(byset)
print(cset)
dset=byset.difference(myset)
print(dset)

# difference_update()
# difference_ update means remove all the elements of another set from this set.
# another set is taken as parameter
# returns a new set,without the unwanted items
#syntax : set.difference_update(another set name)
#example:
myset.difference_update(byset)
print(myset)
byset.difference_update(myset)
print(byset)

# set.discord()
# discord means removes an element from the set,if it is a number.
# element is taken as parameter
# no return
# syntax: set.discord(elements)
# example :
myset.discard(8)
print(myset)

# set.intersection()
# intersection means compare the two sets elements those are common elements return it.
# another set is taken as parameter
# returns a set thar contains the similarity between two or more sets
# syntax : set.intersection(anotherset)
# example :
set1={'a','c','f','h','i'}
set2={'g','h','c','o'}
print(set1.intersection(set2))

# set.intersection_update()
# intersection_update means remove the item in the set that are not present in other,specified set.
# another set is taken as parameter
# returns a new set, without unwanted elements.
# syntax : set.intersection_update(another set)
# example :
set1.intersection_update(set2)
print(set1)

# set.isdisjoint()
# isdisjoint means returns wheather two sets have a intersection or not.
# another set is taken as parameter
# returns a boolean value
# syntax : set.isdisjoint(anotherset)
# example :
print(set1.isdisjoint(set2))

# set.issubset()
# issubset means returns wheather this set contain another set (or) not.
# another set is taken as parameter
#  returns a boolean type
# syntax : set.issubset(anotherset)
# example :
print("subset",set1.issubset(set2))

# set.symmetric_difference()
# symmetric_difference means return a set that contain all elements from both sets,but not the terms that are present in both sets.
# another set is taken as parameter
# return a set that contain all elements from both sets
# syntax : set.symmetric_difference(anotherset)
# example :
set3={"java","python","c++"}
set4={"java","c","sql"}
print("symmetric",set3.symmetric_difference(set4))

# set.symmetric_difference_update()
# symmetric_difference_update means update the orginal set by removing elements that are present in both sets,and inserting other elements.
# another set is taken as parameter
# syntax : set.symmetric_difference_update(anotherset)
# example :
set3.symmetric_difference_update(set4)
print("symmetric_difference_update",set3)

# set.union()
# union means return a set that contain all elements from the original set,and all elements from the specified set.
# another set is taken as parameter
# returns a set
# syntax : set.union(another set)
# example :
set5={1,2,3,4}
set6={4,5,6}
set6=set5.union(set6)
print(set6)

# set.update()
# update means updates the current set,by adding the items from another set
 # another set is taken as parameter.
 # no return value
# syntax : set.update(another set)
# example :
set6.update(set5,set4,set3)
print(set6)

# set.issuperset()
# issuperset means method returns true if all the elements in the specified set exists in the original set,otherwise it returns false.
# another set is taken as parameter
# returns boolean data type
# set.issuperset(anotherset)
# Example :
print(set5.issuperset(set6))















