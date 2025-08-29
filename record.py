class Student:
    college_name = "SCET"
    
    def __init__(self,name,rollno,section,marks):
        self.name = name
        self.rollno = rollno
        self.section = section
        self.marks = marks
        
    def welcome(self):
        print("Hello its your result ", self.name)

        
s1 = Student("Himanshu",40,'A',97)
s1.welcome()
print(s1.name,s1.rollno,s1.section,s1.marks,Student.college_name)