inp=[12,2,15,14]
"FIZZBUZZ"
for num in inp:

    if num%3 == 0 and num%5 == 0:
        print("FIZZBUZZ")
    elif num%5 == 0:
        print("BUZZ")                       
    elif num%3 == 0:
        print("FIZZ")