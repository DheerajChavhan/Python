# Q1 Writ a program to open three files 1.txt,2.txt and 3.txt if any these files are not present,a message without existing a program must be printed promting the same.

# try:

#     with open("1.txt")as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:

#     with open("2.txt")as g:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:

#     with open("3.txt")as h:
#         print(f.read())

# except Exception as e:
#     print(e)


# Q2: Write a program to print third,fifth and seventh element from the list using enumerate function 

# List=[1,2,3,4,5,6,7,8,9]

# for i,item in enumerate(List):
#     if(i==2 or i==4 or i==6):
#         print(item)


# Q3:Write a list comprehension to print a list which contains the multiplication tabe of a user entered number 

# n=int(input("Enter the number:"))
# Table=[n*i for i in range(1,11)]
# print(Table)

# Q4:Wite a program to display a/b where a and b are integers. if b=0 display infinite by handling the "Zero division error" 

# try:
#     a=int(input("Enter the number:"))
#     b=int(input("Enter the number:"))
#     print("The Division of a/b is:",a/b)

# except ZeroDivisionError as v:        
#     print("Infinite")


# Q5:Store the table generated in Q3 in new file name Table.txt 

n=int(input("Enter the number:"))
Table=[n*i for i in range(1,11)]
print(Table)

with open("Tables.txt","a") as f:
    f.write(f"Table of {n}:{str(Table)}\n")
