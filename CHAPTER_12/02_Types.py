from typing import List,Tuple,Dict

Numbers:List[int]=[1,2,3,4,5,6]                                        #To store the list of integers in the variable
People:Tuple[str,int]=["Dheeraj",15]                                   #To store the value of required tuple in variable
Scores:Dict[str,int]={"Rohit Sharma":264,"Virat Kohle":150}            #To store the value of required Dictionary in variable


n:int =5                                                               #Helps to identify the type for the the new user
a:str ="Dheeraj"


def sum(a:int,b:int)->int:                                             #Function
    return a+b

print(n)
print(a)
b=sum(5,6)
print(b)
print(Numbers)
print(People)
print(Scores)
