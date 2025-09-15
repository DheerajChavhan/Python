# Q1: Write a program to find out gratest of the three number using functions

# def greatest(a,b,c):
#     if(a>b and a>c):
#         print(f"{a} is Greatest Number")
#     elif(b>a and b>c):
#         print(f"{b} is Greatest Number")   
#     else:
#         print(f"{c} is Greatest Number")       

# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
# greatest(a,b,c)        

# Q2: Write a program to convert celcius to fahrenheit (°F = (9/5 × °C) + 32.)

# def C_TO_F(a):
#      F = (9/5 * a) + 32
#      return F

# a=int(input(("Enter the Temperature (in deg Celcius): ")))

# print("The Temperature in Farenheit is:",C_TO_F(a))

# Q3:How do you prevent the python print() function to print a new line at the end 

# print("A")
# print("B")
# print("C",end="")
# print("D",end="")

# Q4:Write a recursive function to find the sum of n natural numbers
  
# def sum(n):
#     if(n==1):
#         return 1
#     return n + sum(n-1)

# n=int(input("Enter the number:"))
# print(f"The sum of first {n} number is:{sum(n)}")

# Q5:Write a program which will convert inches to cms(cm=inches×2.54)

# def I_to_CM(inches):
#     cm=inches*2.54
#     return cm

# inches=int(input("Enter the length in inches:"))
# print("The length in centimeters:",I_to_CM(inches))

# Q6:Write a function to print multiplication table

def Table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n=int(input("Enter the number:"))        
Table(n)        

