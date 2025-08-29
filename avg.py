class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hello", self.name, "your average score is:", sum/3)
    
    
    @staticmethod #This is used to makr a staticmethod, this is known as decorator
    def hello():
        print("Hello")   

s1 = Student("Himanshu kaushik", [98,97,96])
s1.get_avg()        
#We can directly change the given attribute
s1.name = "Vaibhav"
s1.marks = [67,56,87]
s1.get_avg()

s1.hello()

#Staticmethod those method which dont requires self

