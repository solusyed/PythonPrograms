res=0
num=5
for i in range(1,num+1):
    if num % i == 0:
        res=res+1
        if res>2:
            break
if res>2:
    print("not a primenumber")
else:
    print(" prime")


def prime_number(start, end):
    for i in range(start, end):
        if(is_prime_number(i)):
            print(i)



def is_prime_number(n):
    for i in range(2, n-1):
        if (n % i ==0):
            return False
    return True

# prime_number(5, 10)
print(is_prime_number(1234))















