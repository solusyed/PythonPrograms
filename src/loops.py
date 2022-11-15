"""
In python we have two loops those are :
loops:
1) for loop
2) while loop

while loop:
    while loop is a pretest loop ,it first test a specified conditional expression ,as long as the condition expression is true it will take
    action,
    while loop is known as " Entry control loop".
    syntax:
    while(condition):
        statement
        """
# example : sum of elements in list while using the while loop
li=[12,24,56,45,85]

leng = len(li)
res = 0
# condition
while(leng != 0):
    res = res + li[leng -1]
    leng = leng -1
    print(res)


# if we want to use for loops ,we must statisfy the three conditions:
#      same process for
#      to reach a result
#      number of times
#      these 3 conditions are satisfied we use for loop.



# for loop :
#  the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
# example:
fruits=["banana","pineapple","grapes"]
for items in fruits:
    print(items)

 # using for loop write a 9 table
num=9
for items in range(1,11):
     print(num, 'x', items ,'=' , num*items )



# note :
     # find the length of the string
list=[5,6,4,7,2,3,]
length=len(list)
print(length)
print(range(length))

# note :
#    range :
   # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1
   # in range we have 3 types of parameters(start ,end ,increment/decrement)
   # example:
print(range(length))
    # example :
for x in range(6):
     print(x)








ls