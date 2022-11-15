res = {
    "name": "fardeen",
    "age": 22,
    "city": "ongole"
}

print('city' in res)


for item in res:
    if item == 'city':
        print("true")


# slicing
li=[1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
print(li[:-1])
print(li[0:])
print(li[1:5])
print(li[::-2])
print(li[:5:2])
print(li[:3:-2])
print(li[12:6:-2])
print(li[-1:10])
print(li[: : -2])
print(li[-5:6])



# palindrome

name="test"
if(name==name[::-1]):
    print("palindrome")
else:
    print("not")


def is_palindrome(name):
    if(name==name[: : -1]):
        return("is palindrome")
    else:
        return("not a palindrome")


print(is_palindrome("test"))
print(is_palindrome("lol"))
print(is_palindrome([1,2,3,2,1]))






