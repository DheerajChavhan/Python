# def avg():               #Creating a function

#     A=int(input("Enter the number: "))
#     B=int(input("Enter the number: "))
#     C=int(input("Enter the number: "))

#     Average=(A+B+C)/3
#     print("The Average of the given numbers is:",Average)

# avg()                     #This is called function call

# def GOODDAY(name,ThankYou):
#     print("Good Day", name)
#     print(ThankYou)
#     return 10    #Helps to store the data in variable

# a=GOODDAY("Dheeraj","Thank You")
# print(a)

# Default Parameter

def greet(name,ending="Thank You"):     #By default value of ending is 'Thank You'.if not provide value while calling it will show
    print(f"Good Day,{name}")
    print(ending)

greet("Dheeraj")
greet("Dheeraj","Thanks")