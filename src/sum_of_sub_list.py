li = [20, 30, 40, 60, 90, 100]
li.sort()
expe = 170





res = []

for i in range(len(li)):
    if expe in li[i+1:]:
        res.append(expe)
        break
    else:
        res.append(li[i])
    expe -= li[i]
    if expe <= li[i+1]:
        res = []
        break

print(res)
