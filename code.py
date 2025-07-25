lst = [1,2,3,2,3,4]
newlst = []
for x in lst:
    if lst.count(x)>1 and x not in newlst:
        newlst.append(x)

