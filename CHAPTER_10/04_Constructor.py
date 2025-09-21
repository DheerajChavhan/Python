
class Employee:
    Name="Dheeraj"  # This is a class attribute
    Language="Python"
    Salary=100000


    def __init__(self,Name,Language,Salary):
        self.Name=Name
        self.Language=Language
        self.Salary=Salary
        print("I am creating an object")   # i am dunder method(starts with __ ) which is automatically starts


    def getInfo(self):
        print(f"The language is {self.Language}.The Salary is {self.Salary}")
    


A=Employee("Dheeraj","Java Script","2500000")
print(A.Name,A.Language,A.Salary)
