class Employee:

    def __init__(self):
        print("It is the constructor of Employee")
    a=1

class Programmer(Employee):

    def __init__(self):
        print("It is the constructor of Programmer")
    b=2

class Manager(Programmer):

    def __init__(self):
        super().__init__()                         #The super key word is used to run the constructor of the base class
        print("It is the constructor of Manager")
    c=3

o=Employee()
o=Programmer()
o=Manager()
