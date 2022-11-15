li1=[1,2,3,4,5]
li2=[2,4,5,6]

li1=set(li1)
li2=set(li2)
print(li1)
print(li2)

li3=li2.difference(li1)
#print(list(li3))


res=[]
for i in li2:     # here considering the i as list2
    if i in li1:# here i is as list 2 checking the lli3=li2.difference(li1)
        li1.remove(i)
    else:
        res.append(i)

    #print(res)

# sum of difference of sibiling elemnets
l1=[20, 30, 50, 90, 100]
# print(len(l1))
res=0
for i in range(len(l1)-1):
    res=res+(l1[i] - l1[i+1])
# print(res)



# sum of differences of sibiling elements in reverse order
li=[20, 30, 50, 90, 100]
print(len(li))
res=0
for i in range(len(li) -1, 0, -1):
    res = res+(li[i] - li[i-1])
    # print(res)
print(res)


# resverse a sting:
num=" first program"
res=""
temp=-1
for i in num:
    res=res+num[temp]
    temp=temp-1
print(res)


dum="this is my first python program"
res=""
for i in range(len(dum)-1, -1, -1):
    res=res+dum[i]
print(res)

