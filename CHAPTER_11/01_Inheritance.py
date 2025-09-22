class Employee:
    company="ITC"

    def show(self):
        print(f"The name of the employee is {self.Name}")

class Programmer(Employee):  #We inherited all the function and methods from Employee and added more given below
    company="ITC Infotech"

    def showLanguage(self):
        print(f"His name is {self.name} and He is good in {self.language}")

a=Employee()
b=Programmer()
print(a.company,b.company)

