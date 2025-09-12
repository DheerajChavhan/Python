# Write a program to craete a dictionary of hindi words with values as their english translation.Provide user with an option to look it up

# words={
#     "Billi":"Cat",
#     "Kutta":"Dog",
#     "Madad":"Help",
#     "Kursi":"Chair"
# }

# word=input("Enter the Hindi word:" )
# print(words[word])

# Write a program to input eight numbers from the user and display all the unique numbers once

# a=set()
# b=input("Enter the number:" )
# a.add(int(b))
# b=input("Enter the number:" )
# a.add(int(b))
# b=input("Enter the number:" )
# a.add(int(b))
# b=input("Enter the number:" )
# a.add(int(b))
# b=input("Enter the number:" )
# a.add(int(b))
# b=input("Enter the number:" )
# a.add(int(b))
# b=input("Enter the number:" )
# a.add(int(b))
# b=input("Enter the number:" )
# a.add(int(b))
# print(a)

# Can we have a set with 18 as string and 18 as int
# s=set()
# s.add(18)
# s.add("18")
# print(s)

#what is the length of the set given below

# s=set()
# s.add(18)
# s.add(18.0)
# s.add("18")
# print(len(s)) #Length is 2 because in python 18.0=18

# what is the type of the following

# d={}
# print(type(d)) #Dictionary

# # Create an empty dictionary.Allow 4 friends to enter their favourite language as value and use keys as their names. assume that their names are unique.

# dict={}

# a=input("Enter your favourite language:" )
# dict.update({"Dheeraj":a})
# b=input("Enter your favourite language:" )
# dict.update({"Prem":b})
# c=input("Enter your favourite language:" )
# dict.update({"Suraj":c})
# d=input("Enter your favourite language:" )
# dict.update({"Ransing":d})

# print(dict)

#what will happen if the names of two friends are same.What will happen to the above program

# dict={}

# a=input("Enter your favourite language:" )
# dict.update({"Dheeraj":a})
# b=input("Enter your favourite language:" )
# dict.update({"Prem":b})
# c=input("Enter your favourite language:" )
# dict.update({"Prem":c})
# d=input("Enter your favourite language:" )
# dict.update({"Ransing":d})

# print(dict)  #The key of the repeated name will be showed once in a set but the last updated value will be shown

# Can you change the values inside the list which is contained in set S={8,7,12,"Dheeraj",{1,2}}

S={8,7,12,"Dheeraj",[1,2]}
S.remove("Dheeraj")
S.add("Prem")
print(S)  #No because lists are immutable which cant be stored in a Set


