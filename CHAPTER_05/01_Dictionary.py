Marks={
    "Dheeraj":100,
    "Prem":75,
    "Ransing":20
}
print(Marks,type(Marks))

print(Marks["Dheeraj"]) #Returns the value of the key "Dheeraj"
print(Marks.items()) #Returns all items
print(Marks.keys()) #Returns the keys 
print(Marks.values()) #Returns the values 
Marks.update({"Dheeraj":99,"Rudra":30})
print(Marks,type(Marks)) #Updated the value of 1st key and added the new key and value

