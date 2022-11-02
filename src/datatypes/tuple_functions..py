"""
Tuple is a one of data type in python
Tuple is a immutable,we can't mmodify the elements in tuple.
Tuples are used to store multiple items in a single variable.
 A tuple is a collection which is ordered and unchangeable.
 Tuple is defining in parenthesies ().
 Tuple we have two methods,those are:
 1) count     2) index
"""
# example:
num=(1,45,52.5,56,)
print(num)

# 1.count()
# count() method means  returns the number of times a specified value appears in the tuple.
# element is taken as parameter
# it returns the element.
# syntax : tuple.count(element)
# example :
thistuple=(1,2,3,4,5,2,3)
b=thistuple.count(3)
print(b)

# 2.index()
# The index() method finds the first occurrence of the specified value.
# elements is taken as parameter.
# it returns the index value
# syntax:
#     tuple.index(elements)
# example:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(6)

print(x)