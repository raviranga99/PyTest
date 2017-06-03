t1=("r","a","v","i")
t2=(2,5,8,9)
print t1,t2

"""Following action is not valid for tuples 
#Tuples are immutable which means you cannot update or change the values of tuple
elements. You are able to take portions of existing tuples to create new tuples as the
followi"""

#   t1[1]=22
"""# So let's create a new tuple as follows"""
t3=t1+t2
print t3

"""Removing individual tuple elements is not possible."""
"""delete whole tuple"""
#del t1
print t1
"""-------method-----------------------"""
print len(t1)

print len(t2)
print max(t2)
print min(t2)
"""-----change tuple into list"""
l=list(t1)
print l