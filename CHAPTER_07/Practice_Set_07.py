# Q1: Write a program to print multiplication table of a given number using a for loop.

Table=int(input("Enter the Table Number:" ))

for i in range(1,11):
    print(Table , "x", i ,"=" ,Table*i)
    i=i+1

#Q2: Write a program to greet all person present in the list and which starts with S
L=["Dheeraj","Suraj","Prem","Shravan"]
 
L=["Dheeraj","Suraj","Prem","Shravan"]

for i in L:
    if(i[0]=="S"):
        print("Have a nice Day",i)

# Q3: Attemp Q1 using while loop 

Table=int(input("Enter the Table Number:" ))

i=1
while(i<=10):
    print(Table , "x", i ,"=" ,Table*i)
    i=i+1

# Q4: Write a program to find whether the number is prime or not 

Number = int(input("Enter the number: "))

for i in range(2,Number):
    if(Number%i==0):
        print("The number is not prime")
        break
    else:
        print("The number is prime")
        break

# Q5: Write a program to find the sum of first n number using while loop 

N=int(input("Enter the number: "))

i=1
Sum=0
while(i<=N):

    Sum=Sum+i
    i=i+1

print("The Sum of the first",N,"Numbers are: ",Sum)  #The print function should be out of the loop

# Q6: Write a program to find the factorial of the given number using the for loop 
n=int(input("Enter the number: "))

product=1

for i in range(1,n+1):
    product=product*i
    i=i+1
print("The factorial of given number is:",product)

# Q7: Write a program to print multiplication table of n using for loops in reveresed order

Table=int(input("Enter the Table Number:" ))
for i in range(1,11):
    print(Table , "x", 11-i ,"=" ,Table*(11-i))
    i=i+1
