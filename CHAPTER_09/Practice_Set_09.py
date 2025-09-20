# Q1: write a program  to read the txt from the given file "poems.txt" and find out whether it contains the word twinkle. 

with open("poems.txt") as f:
    content=f.read()
    if "Twinkle" in content:
        print("Yes the word Twinkle is present")
    else:
        print("NO the word Twinkle is not present")

# Q2: Game() function in a program lets a user play a game and returns the score as an integer.You need to read a file "Hi_Score.txt"
# which is either blank or contains the previous high score.You need to write a program to update the Hi-score whenever the game() function
# breaks the Hi-score

import random
def Game():
    print("You are Playing a game")
    score=random.randint(1,101)
    with open("Hi_Score.txt") as f:
        Hi_Score=f.read()
        if(Hi_Score!=""):
            Hi_Score=int(Hi_Score)
        else:
            Hi_Score=0   

    print("Your Score is:",score)
    if(score>Hi_Score):
        with open("Hi_Score.txt","w") as f:
            f.write(str(score))
         
Game()

# Q3: Write a program to generate multiplication tables from 2 to 20 and write it to the different files.place these files in a different file.
 
def GenerateTable(n):
    Table="" 
    for i in range(1,11):
        Table=Table+ f"{n} x {i}  = {n*i}\n"
    
    with open(f"Tables/Table_{n}.txt", "w") as f:
        f.write(Table)

for i in range(2,21):
    GenerateTable(i)
    
# Q4:A file contain a word "Donkey" multiple times.You need to replace this word with "####" by updating the same file 

word="Donkey"
with open("Donkey.txt") as f:
    content=f.read()
contentNew=content.replace(word,"#####")

with open("Donkey.txt","w") as f:
    f.write(contentNew)

# Q5:Repeat Q4 for a list of such words to be censored    

words=["Donkey","bad","ganda"]
with open("Donkey.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#"*len(word))

with open("Donkey.txt","w") as f:
    f.write(content)

# Q6: Write a program to mine a log file and find out whether it conains python

with open("log.txt") as f:
    content=f.read()

if("python" in content):
    print("Yes The file contains the word python ")
else:    
    print("No The file does not contains the word python ")

# Q7: Write a program to make a copy of the text file "This.txt"

with open("This.txt") as f:
    content=f.read()

with open("This_copy.txt","w") as f:
    f.write(content)

# Q8: write a program to find out whether a file is identical and matches the content of another file 

with open("This.txt") as f:
    content1=f.read()

with open("This_copy.txt") as g:
    content2=g.read()

if(content1==content2):
    print("Both the file are identical")
else:    
    print("Both the file are not identical")

# Q9: Write a program to wipe out the content from the file

with open("This.txt","w") as f:
    f.write("")

