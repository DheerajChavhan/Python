try:
    a=int(input("Enter the number:"))
    print(a)

except Exception as e:
    print("Enter the valid number!")
    
else:
    print("I am inside else")      #This will run only when try is successful



    