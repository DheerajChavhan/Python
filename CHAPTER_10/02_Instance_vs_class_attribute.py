class Employee:
    Name="Dheeraj"  # This is a class attribute
    Language="Python"
    Salary=100000

A=Employee()
A.place="Pune"      #This is a object/instance attribute
A.Salary=200000     #The value of instance attribute is preferred more than class attribute
print(A.place,A.Name,A.Salary)
