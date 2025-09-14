def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("Enter the number:"))
print("Factorial of the given number is:",factorial(n))