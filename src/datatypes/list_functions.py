"""
List is a one of the data type in python.
list is defined as the sequence data type which is used to store the collection of data.
list is defining in square brackets [].
In list, we can store different types of data.
eg; (integer,string)
In list, we can store duplicate elements also.
In list every element store by index(position)
In list,  number of elements-1 = last index
They are: list.append(),list.remove(),list.insert(),list.pop() etc
list is mutable, modify the data in list (share the same memory, with two diff names)

"""
# example

num_list = [1, 2, 3, 4, 5, 'a']
# list Methods :
# 1.list.append()
# append means adding an element to the list .while using append method in list the element was added in the last element in the list.
# list.append method , default value is considering as the  adding the element as a last element in that list.
# element is taken as parameter
# no return
# syntax: list.append()
# example:
num_list.append(6)
print(num_list)
# 2.list.remove()
# remove means removing the element in the list.
# IN remove method we give the which element we want to remove.
# In remove method no return elements
# element is taken as parameter
# syntax: list.remove(element)
# example:
num_list.remove(2)
print(num_list)
# 3. list.pop()
 # pop means deleting a element in the list.
 # IN pop we want to delete a element in the list , we must specify the index number of that element.
 # pop returns a removed  element
 # pop takes position as parameter.
 # syntax: list.pop(index value)
 # example:
print(num_list.pop())
# 4. list.reverse()
 # reverse means reversing a list.
 # no returns a element
 # no parameter
 #syntax: list.reverse()
 # example:
num_list.reverse()
print(num_list)
# 5.list.copy()
 # copy means it returns the copy of list.
 # no parameters
 # returns a copied list
 # syntax: list.copy()
 # example:
copy_num_list = num_list.copy()
print(copy_num_list)
copy_num_list.append(9)
print(copy_num_list)
print(num_list)
# 6.list.clear()
 # clear means it removes all elements in the list.
 # no return
 # no parameter
# syntax:list.clear()
# example:
num_list.clear()
print("clear",num_list)
# 7.list.count()
 # count means counting the number of occurances.
 # element taken as parameter
 # it returns the elements
 # syntax: list.count(elements)
 # example:
sec_list=[1,2,2,3,4]
temp_list=sec_list.count(2)
print(temp_list)
# 8.list.sort()
 # sort means sorting the elements.
 # IN sort default order is ascending order.
 # IN sort parameters is taken as reverse and key.
 # no return
 # syntax:list.sort()
 # exampole:(descending order)
d=[1,4,7,6,5,9]
d.sort(reverse=True)
print(" sort",d)
# example: by default ascending order
d.sort()
print(d)
# example 2:
# sorting a list which have a string elements
list=['c','b','d','h','i','j','l']
list.sort()
print(list)
# 9.list.insert(position,values)
 # insert means inserting the elements in a list with position value
 # position and value is taken as parameters
 # no returns
 # syntax: list.insert(position ,value)
 # example 1 :
d.insert(3, 10)
print(d)
# 10.list.index()
# index means returns the index of first element with specified value.
# elements is taken as parameters
# it returns the index value
# syntax: list.index(elements)
# example:
mylist=[1,2,3,4]
print(mylist.index(3))
# 11.list.extend()
# extend means add a element of a list(or)add two list into one list
# iterable (list,set,tuple,etc) taken as parameter.
# no return
# syntax: list.extend(iterable)
# example:
num=[1,2,3,4]
value=[5,6,7,8]
num.extend(value)
print(num)





