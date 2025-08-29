# class Student:
#     name = ["Himanshu Kaushik","Neha Kaushik"]
#     rollno = 21343557
# # creating an object (instance)
# #object variable = class-name()
# s1 = Student()
# print(s1.name[0])
# print(s1.rollno)

# s2 = Student()
# print(s2.name[1])

class Car:
    brand = "Honda"
    color = "Black"
    model = "Automatic Civic"
    
car1 = Car()
print(car1.brand) 
print(car1.color) 
print(car1.model) 

#constructor __init__ Function
class Student():
    #class attribute
    college_name = "SCET"
    def __init__(self,name,rollno,section):# in constructor there should be a parameter called self always
       #these all are object attributes
        self.name = name
        self.rollno = rollno
        self.section = section
        
        #here the variable with name as name is created and takes the value of fullname
        
#creating an object s1
s1 = Student("karan",98765,"B")
print(s1.name,s1.rollno,s1.section,Student.college_name)

s2 = Student("Himanshu",56789,"A")
print(s2.name,s2.rollno,s2.section,Student.college_name)

#Attribute : the variables are used in classes and objects are known as attributes
# There are two types of attributes :
#1. Class attribute : Those attributes which is same for each and every object is known as class attribute
#2. Object attributes are those whose value is change for every object this is declaired by using self.attribute-name in constructor

#Methods are functions that belongs to objects

class Bike:
    
    def __init__(self,model):
        self.model = model
        
    def hello(self):
        print("It is a Bike ", self.model)
        
    def sum(self,num1,num2):
        sum = num1+num2
        print(sum)

b1 = Bike("Honda")
b1.hello()
b1.sum(6,7)