siz = 4

numbes = ['L', 'D', 'D',' L']

count =0
for each in range(siz):
    if numbes[each] == 'D':
        numbes[each] = 'L'
        if each+2 <= siz:
            numbes[each+1], numbes[each+2] = numbes[each+2], numbes[each+1]
        count += 1

print(count)