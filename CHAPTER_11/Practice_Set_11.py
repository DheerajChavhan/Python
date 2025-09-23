#Q1: Create a class 2-D vector and use it to create another class representing 3-D vector

class two_d_vector:

    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The 2-D Vector is {self.i}i+{self.j}j")  
 

class three_d_vector(two_d_vector):

    def __init__(self,i,j,k):
       super().__init__(i,j)     #IMP: We never write self inside the super function
       self.k=k

    def show(self):
        print(f"The 3-D Vector is {self.i}i + {self.j}j + {self.k}k")  

a=two_d_vector(5,6)
a.show()
b=three_d_vector(1,6,8)
b.show()


# Q2:Create a class Pets from the class Animals and further create a class Dog from pets.Add a method bark to class Dog. 

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("The dog is barking")

a=Dog()
a.bark()


# Q3: Create a class Employee and add salary and increment properties to it.
# Write a method 'salaryafterincrement method with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    Salary=100000
    increment=10

    @property
    def salaryafterincrement(self):

        return self.Salary + self.increment*self.Salary/100
    
    @salaryafterincrement.setter             #It allow to give the value to the attribute

    def salaryafterincrement(self,Salary):
        self.increment=((Salary/self.Salary)-1)*100


a=Employee()
a.salaryafterincrement=110000
print(a.increment)
print(a.salaryafterincrement)


# Q4: Write a class complex to represent complex numbers along with overloaded operator the + and * operator which calculates the sum and the dot product of them.


class complex :
    i=(-1)**(1/2)

    def __init__(self,a,b):

        self.a=a
        self.b=b
        
    
    def __add__(self,other):

        return complex(self.a+ other.a, self.b+other.b)
    
    def __mul__(self,other):

        return self.a * other.a + self.b * self.i  * other.b *self.i

    def __str__(self):
        return(f"{self.a}+{self.b}i" )
    
c1=complex(1,2)
c2=complex(3,4)

print("Sum:",c1+c2)
print("Product:",c1*c2)


# Q5: Write a class vector representing a vector of n dimentions. overload the + and * operator which calculates the sum and dot product of them 

class vector :
   
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def __add__(self,other):
        return vector(self.a+ other.a, self.b+other.b,self.c+other.c)
    
    def __mul__(self,other):
        return vector(self.a * other.a , self.b * other.b, self.c * other.c )

    def __str__(self):
        return(f"{self.a}i+{self.b}j+{self.c}k" )
    
c1=vector(1,2,3)
c2=vector(3,4,5)

print("Sum:",c1+c2)
print("Product:",c1*c2)


# Q6:Write a __str__ method to print the verctors as follows: 7i+8j+10k

class vector :
   
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return f"{self.a}i+{self.b}j+{self.c}k"    

V=vector(7,8,10)
print("The vector is:",V)


# Q7: Override the len method on vector of problem 5 to display the dimention of the vector 

class vector :
   
    def __init__(self,l):
        self.l=l

    def __len__(self):
        return len(self.l)
        
V=vector([1,2,3,4])     
print("The length of Vector is:",len(V))