class Employee:
    Name="Dheeraj"  # This is a class attribute
    Language="Python"
    Salary=100000

    def getInfo(self):
        print(f"The language is {self.Language}.The Salary is {self.Salary}")
    

A=Employee()
A.getInfo()
