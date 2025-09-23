class Employee:
    
    A=1
    def show(self):
        print(f"The value of A is:{self.A}")

e=Employee()
e.A=25      
e.show()       #It will show A=25 because it is instance attribute


class Employee:

    A=1 
    @classmethod
    def show(cls):
        print(f"The value of A is:{cls.A}")

e=Employee()
e.A=25      
e.show()       #It will show A=1 because @class method gives priority to class attribute