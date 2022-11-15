"""
Conditions statements:
In pyhon condidtion statements are if,elif,else
if statement:
syntax:
if(condition):
statement
An "if statement" is written by using the ifkeyword.
In python if statement is a conditional statement.
in if statement the condition was true,then the statements was executed by step by step.
the if statement was only accepted the true conditions.
if the condition was true then it returns the boolean value.
"""
# example :
age=20
if(age >= 10):
    print("SOhail")

    # else statement:
# else is also a condition statement.
# else statement is defined as the the if statement is false ,then else statement was executed.
# example:
a=56
b=45
if(a<=b):
        print("b is greater than a")
else:
        print("a is greater than b ")

 # elif statement:
 # The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition.
 # example:
d=33
e=33
if(d>e):
    print("d is greater than e")
elif(d==e):
    print(" d is equals to e")
else:
    print(" e is greater than b")
