 # Q1) Write a program to find the greatest of the four numbers entered by the user
First=int(input("Enter the First number:"))
Second=int(input("Enter the Second number:"))
Third=int(input("Enter the Third number:"))
Fourth=int(input("Enter the Fourth number:"))

if( First>Second and First>Third and First>Fourth):
    print("First number is greatest among all")

elif(Second>First and Second>Third and Second>Fourth):
    print("Second number is greatest among all")   

elif(Third>First and Third>Second and Third>Fourth):
    print("Third number is greatest among all")     

else:
       print("Fourth number is greatest among all")    

# Q2) Write a program to find out whether a student is passed or failed if it requires a total 
# of 40% and atleast 33% in each subject to pass.Assume 3 sujects and take marks as an input from the user

S1=int(input("Enter the marks of Subject1: "))
S2=int(input("Enter the marks of Subject2: "))
S3=int(input("Enter the marks of Subject3: "))

Total=300
Percent=(S1+S2+S3)/Total*100
Percentage=print("Percentage is:" , Percent)

if(Percent>=40 and S1>=33 and S2>=33 and S3>=33):
     print("Student is Passed")

else:
     print("Student is Failed")     

#Q3) A spam comment is defined as a text containing following keywords:
# "Make a lot of money","buy now","subscribe this","click this".Write a program to detect these spam     

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

Message=input("Enter your Comment:" )

if((p1 in Message) or (p2 in Message) or (p3 in Message) or (p4 in Message)):
     print("Message is a SPAM")
else:
    print("Message is NOT a SPAM")   

#Q4) Write a program to find whether the username has less than 10 characters or not.

username=input("Enter the Username: ")
if(len(username)<10):
     print("The length of the username is less than 10")
elif(len(username)==10):
     print("The length of the username is 10")   
else:
     print("The length of the username is greater than 10")        

# Q5) Write a program to find out whether the given name is present in the list or not.

A=["Dheeraj","Prem","Suraj","Aman"]
Name=input("Enter Your name: ")     

if(Name in A):
    print("Yes! Your name is in the list.")
else:    
    print("No! Your name is not in the list.")

# Q6) Write a program to calculate the garde of the student from his mark from the following scheme

# 90-100=>Ex
# 80-90=>A
# 70-80=>B
# 60-70=>C
# 50-60=>D
#  <50 =>F

Marks=int(input("Enter Your marks: "))

if(Marks >= 90 and Marks<=100):
    print("Your grade is Excellent")

elif(Marks >= 80 and Marks<90):
    print("Your grade is A")
    
elif(Marks >= 70 and Marks<80):
    print("Your grade is B")     

elif(Marks >= 60 and Marks<70):
    print("Your grade is C")   

elif(Marks >= 50 and Marks<60):
    print("Your grade is D")   

elif(Marks > 100 or Marks<0):
    print("Your entered marks are incorrect")        
   
else:
    print("Your grade is F")

# Q7)Write a program to find out whether the given post is takling about Dheeraj or not    

post=input("Enter the post: ")

if("Dheeraj" in post):
    print("Yes! This post is Talking about Dheeraj")
else:
    print("No! This post is NOT Talking about Dheeraj")
