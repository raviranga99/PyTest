# 1  show whole list
l= [1, 5, 8]
print "print whole list---",l
print "after 1--- ",l[1:]
print "",l[2:3]
"""--------Built-in List Functions and Methods---------------------------"""
print "lenght----",len(l)
print "maximum---",max(l)
print "minimum---",min(l)
# add and replace an ele any where in the list
l[1]=7
print "add and replace an ele any where in the list----",l

# del an element any where in the list
del l[2]
print "delete ele---",l


"""-----------Methods with Description---------------"""
#add ele at last l.append(ele)
l.append(4)
print l

# count an ele how many time it exit in list
print l.count(1)

# add list2 in list1 through extend method
l2=["r","a","v","i"]
l.extend(l2)
print l

#fin the index of an ele
print l.index(4)

# insert ele but not replace insert(index,ele)
l2.insert(1,3)
print l2
# pop method remove though index-----see remove method
l2.pop(1)
print l2
l2.pop()
print l2#by defoult remove at last
print l2.reverse()
"""---change into tuples---"""
t=tuple(l)
print t