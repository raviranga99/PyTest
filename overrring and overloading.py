#-------------------------------------------------------overriding----------------------------------------------------
class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print self.a
        print "paren constructor"
    def __str__(self):
        return 'Vector (%s, %d)' % (self.a, self.b)
    def ss(self):
        print "hello parent"

class Child:
    def __init__(self):
     print "child constructor"
    def ss(self):
        print "hello child"
c=Child()
a=Parent("rrr",7)
print a
c.ss()


"""--ovelriding-------when 2 same func in 2 different class
--overloading ----in a same class same name's many fun but diff args

if we delete  this func 
{ def ss(self):print "hello child }
from child class then c.ss() call parent class ss() func

"""
