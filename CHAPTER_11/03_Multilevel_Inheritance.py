class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3

o=Employee()
print(o.a)
print(o.b) #It will give error because it does not have 'b' attribute
print(o.c) #It will give error because it does not have 'c' attribute

o=Programmer()

print(o.a)
print(o.b)
print(o.c)  #It will give error because it does not have 'c' attribute

o=Manager()

print(o.a)
print(o.b)
print(o.c)
