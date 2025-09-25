a=int(input("Enter a number:"))
b=int(input("Enter a number:"))

if b==0:
    raise ZeroDivisionError("Hey our program is not meant to divide by zero")    #Use to give custom error
else:
    print("The Division of the numbers is",a/b)



    