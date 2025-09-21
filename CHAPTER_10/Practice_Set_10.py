# Q1: create a class Programmers for storing the data of few Programmers working at Microsoft

class Programmers:
    company="Microsoft"

    def __init__(self,Name,Place,Salary):
        
        self.Name=Name
        self.Place=Place
        self.Salary=Salary

A=Programmers("Dheeraj","Pune",100000)
B=Programmers("Prem","Sambhajinagar",200000)
C=Programmers("Suraj","Mumbai",30000)

print(A.Name,A.Place,A.Salary)
print(B.Name,B.Place,B.Salary)
print(C.Name,C.Place,C.Salary)

# Q2:write a class Calculator capable of finding Square,cube and square root of the number

class Calculator:
    def __init__(self,n):
        self.n=n

    def Square_Root(self):
       print(f"The Square Root of the number is :{self.n**(1/2)}")

    def Square(self):
       print(f"The Square of the number is :{self.n**2}")

    def Cube(self):
       print(f"The Cube of the number is :{self.n**3}")

n=int(input("Enter the number:")) 
a=Calculator(n)    
a.Square_Root()
a.Square()
a.Cube()

# Q3: Create a class with a class Attribute a;create a object fron it and set a directly using object.a=0.Does it change the class Attribute

class Atrribute:
   a=1

object=Atrribute()
print(object.a)    #Prints the class attribute because inctanse attribute ws not present
object.a=0
print(object.a)    #Prints the instance atribute
print(Atrribute.a) #Prints the class attribute because only the inctance attribute was created but not changed

# Q4: Add a staticmethod in Q2, to greet the user with hello

class Calculator:
    def __init__(self,n):
        self.n=n

    def Square_Root(self):
       print(f"The Square Root of the number is :{self.n**(1/2)}")

    def Square(self):
       print(f"The Square of the number is :{self.n**2}")

    def Cube(self):
       print(f"The Cube of the number is :{self.n**3}")
    
    @staticmethod    #Static method is used when er don't use any attribute from the function and we don't use self
    def greet():
       print("Hello!")

n=int(input("Enter the number:")) 
a=Calculator(n)    
a.greet() 
a.Square_Root()
a.Square()
a.Cube()

# Q5: Write a class train which has methods to book a ticket,get status(no. of seats) and get fare information of train running under Indian Railways. 
import random
class Train:

    def __init__(self,TrainNo):
        self.TrainNo=TrainNo

    def Book_Ticket(self,fro,to):
        
        print("The ticket is booked in Train Number:",self.TrainNo)
        print(f"The Journey is from {fro} to {to}")
        
    def get_status(self):
        
        print(f"The Train {self.TrainNo} is successfully running on time")
        
    def get_Fare(self,fro,to):    #For Price of the Ticket
        
        print(f"The Ticket fare in Train {self.TrainNo} from {fro} to {to} is {random.randint(1,101)}")
    
A=Train(12345)
A.Book_Ticket("Pune","Beed")
A.get_Fare("Pune","Beed")
A.get_status()

# Q6:Can you change the self parameter inside a class to something else (say "Dheeraj").Try changing self to slf or "Dheeraj and see effects" 

import random
class Train:

    def __init__(slf,TrainNo):
        slf.TrainNo=TrainNo

    def Book_Ticket(slf,fro,to):
        
        print("The ticket is booked in Train Number:",slf.TrainNo)
        print(f"The Journey is from {fro} to {to}")
        
    def get_status(slf):
        
        print(f"The Train {slf.TrainNo} is successfully running on time")
        
    def get_Fare(slf,fro,to):    #For Price of the Ticket
        
        print(f"The Ticket fare in Train {slf.TrainNo} from {fro} to {to} is {random.randint(1,101)}")
    
A=Train(12345)
A.Book_Ticket("Pune","Beed")
A.get_Fare("Pune","Beed")
A.get_status()

# There is no effect whether we use self or slf but you have to use it everywhere