"""
# dictionary is one of data type in python.
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# dictionary is defining in curly brackets{}
# in dictionary we can have different types of methods.
"""


 # example:
num={1:"sohail",2:"fardeen",3:"dileep"}
print(num)

# 1) clear()
# clear() method means removes all the elements from a dictionary.
# no parameters
# no return elements
# syntax:
  #      dictionary.clear()
  # example :
num={1:"sohail",2:"fardeen",3:" dileep"}
num.clear()
print(num)

 # 2) copy():
 #  copy() method means returns a copy of the specified dictionary.
 # no parameters
 # It returns the copied dictionary
 # syntax: dictionary.copy()
 # example:
fam={1:"sohail",2:"fardeen",3:" dileep"}
print(fam.copy())


# 3) fromkey()
#  fromkeys() method returns a dictionary with the specified keys and the specified value.
# keys, and elements taken as parameter.
# it returns the keys
# syntax : dictionary.fromkey()
# example :
sam={1:"sohail",2:"fardeen",3:" dileep"}
print(sam.fromkeys(sam))


# 4) get():
#  get() method returns the value of the element with the specified key.
#   keys and elements taken as parameters.
# it returns the element
# syntax : dictionary.get()
# example :
mam={1:"sohail",2:"fardeen",3:" dileep"}
print(mam.get(3))

# 5) item()
# item()  method means returns a view object,The view object contains the key-value pairs of the dictionary.
# no parameter
# it returns the elements
# syntax : dictionary.items()
# example:
car = {
  "brand": "Ford","model": "Mustang","year": 1964}
x = car.items()

car["year"] = 2018

print(x)

# keys()
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
# no parameters
# it returns the key values
# syntax :
  #     dictionary.keys()
  # example:
car = {
  "brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()

print(x)

# pop()
# The pop() method removes the specified item from the dictionary.
# keys as parameter
# it returns the elemenets
# syntax:
   # dictionary.pop()
  # example:
car = {
  "brand": "Ford","model": "Mustang","year": 1964}
print(car.pop("model"))

# pop item()
# The popitem() method removes the item that was last inserted into the dictionary.
# The removed item is the return value of the popitem() method, it returns in a tuple.
# no parameters
# syntax:
#  dictionary.pop(item)
# example :
car = {"brand": "Ford","model": "Mustang","year": 1964}
print(car.popitem())

# update()
# The update() method inserts the specified items to the dictionary.
# iterable is taken as parameter
# no return value
# syntax :
#      dictionary.update()
# example :
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


# values()
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
# no parameters
# it returns the elements
# syntax:
# dictionary.values
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.values())

# setdefault()
# The setdefault() method returns the value of the item with the specified key.If the key does not exist, insert the key, with the specified value,
# keys and values taken as parameters
# it returns the elements
# syntax:
 # dictionay.setdefault()
 # example :
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.setdefault(" model" ,"ferrari"))
