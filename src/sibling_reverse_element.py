#sum of the difference of the sibbling of reverse element
li= [20,30,50,80,100]

result = 0
for i in range(len(li)-1,0,-1):
    result = result + (li[i] - li[i-1])

print(result)

#reverse a string
num="this my firt program"
res=""
temp=-1
for i in num:
    res=res+num[temp]
    temp=temp-1
print(res)


dum="dileep kumar"
res=""
print(len(dum))
print(range(len(dum)))
for i in range(len(dum)-1, -1, -1):
    res=res+dum[i]
print(res)

ri="this is my car"
re=""
print(len(ri))
print(range(len(ri)))
for i in range(len(ri)-1,-1,-1):
    re=re+ri[i]
print(re)

ti = "this is my first car"
ress=''
for i in range(len(ti)-1,-1,-1):
    ress=ress+ti[i]
    print(ress)