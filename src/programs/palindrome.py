def possible_count_of_pallindrom(str):
    n = len(str)
    str = list(str)

    # loop through character of string
    count = 0
    for i in range(n//2):
        if str[i] != str[n - i - 1]:
            count += 1

    return count

print(possible_count_of_pallindrom('aab'))