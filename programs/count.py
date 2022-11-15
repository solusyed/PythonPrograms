siz=4
numbes=['L', 'D', 'D', 'L']
count=0
for each in range(siz):
    if numbes[each]=='D':
        numbes[each]='L'
        if each+2<=siz:
            numbes[each+1],numbes[each+2]=numbes[each+2],numbes[each+1]
            count=count+1
            print(count)

# fizzbuzz
inp = [12,34,56,15,5,3,4,6]
for num in inp:
 if num%3 ==0 and num%5 ==0:  # ACtual ga num%15==0:
     print("FIZZBUZZ")                                     # print("FIZZBUZZ")
 elif num%5 ==0:
     print("BUZZ")
 elif num%3==0:
     print("FIZZ")
 else:
     print("enter valid number ")


