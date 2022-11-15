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
print(is_palindrome([1,4,3,2,1]))
print(is_palindrome([1,[2,3],4,[3,2],1]))

