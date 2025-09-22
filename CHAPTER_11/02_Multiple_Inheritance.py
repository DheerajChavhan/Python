class Employee:
    company="ITC"

    name=input("Enter Your name: ")
    def show(self):
        print(f"The name of the company is {self.company}")

class coder:
    language="Python"
    def printlanguages(self):
        print(f"Out of all Languages here is your language:{self.language}")        

class Programmer(Employee,coder):  #We inherited all the function and methods from Employee and added more given below
    company="ITC Infotech"

    def showLanguage(self):
        print(f"His name is {self.name} and He is good in {self.language}")

a=Employee()
b=Programmer()
b.show()
b.printlanguages()
b.showLanguage()
