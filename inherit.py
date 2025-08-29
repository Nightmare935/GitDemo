#Inheritance : when one class(child/derived) derives the properties and methods of another class(parent/base)

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
        
#     @staticmethod
#     def stop():
#         print("car stoped..")
        
# class ToyotaCar(Car):    # car class is parent and then all the method of car is inherired in class ToyotaCar
    
#     def __init__(self,name):
#         self.name = name
        
        
# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.start()) #There is any function present in class toyotacar such as name start but due to inheritance it uses the method present in class Car

# There are three types of inheritance :
# 1. Siingle Inhertance , the above example is of single inheritance
# 2. Multi-level Inheritance
# 3. Multiple Inheritance


# 2. This is the example of multi level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")
        
#     @staticmethod
#     def stop():
#         print("car stopped...")
        
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand
        
# class FortunerCar(ToyotaCar):
#     def __init__(self,type):
#         self.type = type
        
        
# car1 = FortunerCar("diesel")
# car1.start()   

# 3. multiple inheritance

class A:
    name = "Happy"
    
class B:
    surname = "Kumar"
    
class C(A,B):
    def __init__(self,fullname):
        self.fullname = fullname
        
p1 = C("Himanshu Kaushik")
print(p1.fullname)
print(p1.name,p1.surname)

# Super_method: Super means parent class

class Car:
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car started..")
        
    @staticmethod
    def stop():
        print("Car stopped..")
        
class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type) # here the type method is directly called from parent class
        self.name = name
        super().start()
        
car1 = ToyotaCar("Fortuner","Diesel")
print(car1.name,car1.type)


# Class_method:
