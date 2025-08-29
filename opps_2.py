class Student:
    def __init__(self,name):
        self.name = name
        
s1 = Student("himanshu")
print(s1.name)

#del keyword is used to delete an objects property or entire object
#del s1.name #This is how an attribute is deleted 
#del s1 #This is how an object is deleted
#print(s1.name)

#how to create private attributes and private methods :
# the private meaning bassically the attribute or method can only be accesed in class 

class Person:
    __name = "anonymous" #this is how a private attribute created
    
    def get_name(self):
        return self.__name
    
    
p1 = Person()
print(p1.get_name())
