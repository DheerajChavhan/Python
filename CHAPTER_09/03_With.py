f = open("file.txt")
Data=f.read()
print(Data)
f.close()

# The above can be also written in the form present below without using f.close()

with open("file.txt") as f:

    Data=f.read()
    print(Data)
