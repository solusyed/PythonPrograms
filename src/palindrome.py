def possible_count_of_pallindrom(str):
    n = len(str)
    str = list(str)

    # loop through character of string
    count = 0
    for i in range(n//2):
        if str[i] != str[n - i - 1]:
            count += 1

    return count

print(possible_count_of_pallindrom('aabccdd'))
#largest number
num=list(str(14355))
num.sort(reverse=True)
print(num)
result=0
for i in num:
    result=result*10+int(i)
print(result)