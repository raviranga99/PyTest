"""What did '*' do?
    It unpacked the values in list 'l' as positional arguments.
    And then the unpacked values were passed to function 'fun' as positional arguments."""
#example 1
def s(a,b,c,d):
    print a,b,c,d
#l[3,5]
l=[1,4,5,5]
s(*l)
#its show an error if we use "l[3,5]" so we use *args
"""It recieves a tuple containing the positional arguments beyond the formal parameter list. So, "args" is a tuple"""
#example 1.1
def ss(*args):
    print args
ss(1,2,4)
def s3(a,*args):
    print a,"and",args
s3(1,4,5,6)
s3(1)

"""What did '**' do? """
#example 2
def s4(a,b):
    print a,b
d={"a":1,"b":2}
#d={"a":1,"b":2,"c":3}      its show an error  so we use *kwargs
s4(**d)
"""What does "**kwargs" mean when used in a function definition?
    kwargs receives a dictionary containing all the keyword arguments beyond the
     formal parameter list. Remember 'kwargs' will be a dictionary."""
#example 2.1
def s5(**kwargs):
    print kwargs
s5(a=4,v=4,f=5)

"""A practical example of where we use 'args', '*kwargs' and why we use it.
Whenever we inherit a class and override some of the methods of inherited class,
 we should use '*args' and '**kwargs' and pass the received positional and keyword arguments to the superclass method."""
"""
class Model(object):
     def __init__(self, name):
            self.name = name
        def save(self, force_update=False, force_insert=False):
            if force_update and force_insert:
                raise ValueError("Cannot perform both operations")
            if force_update:
                #Update an existing record
                print "Updated an existing record"
            if force_insert:
                #Create a new record
                print "Created a new record"
class ChildModel(Model):
    def save(self,*args,**kwargs):
        if self.name=='abcd':
            super(ChildModel,self).save(*args,**kwargs)
        else:
            return None
c=ChildModel('abcd')
c.save(force_update=True)
"""
"""So we need to call the "save()" method of superclass from save()
method of ChildModel. Also, save() method of subclass i.e ChildModel
should be able to accept any arguments that save() of superclass
accepts and must pass through these arguments to the superclass save().
 So we have "*args" and "**kwargs" in the argument list of subclass save()
 method to receive any positional arguments or keyword arguments beyond the formal parameter list."""
