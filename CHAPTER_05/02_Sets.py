a={1,2,3,4}
print(type(a))
b=set() #This means empty set set{} means empty dictionary
c={1,2,3,4,5,6,6,5,4,3,2} #Repeated values is only projected once
print(c)

# Sets Methods
d={1,2,3,4,"Dheeraj"} #String can be a part of set
print(d,type(d))
d.add(10)             #Added the new element
print(d,type(d))
print(len(d))  #Print the length of d
d.remove(1)  #Remove the element 
print(d)

# Union and Intersection

a={1,2,3,4,5}
b={5,6,7,8}
print(a.union(b))
print(a.intersection(b))