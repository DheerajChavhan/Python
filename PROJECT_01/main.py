import random
# 1 for snake ,-1 for water,0 for gun
for i in range(6):
        computer=random.choice([-1,0,1])
        youstr=input("Enter Your Choice:")
        youdict={"s":1,"w":-1,"g":0}
        reversedict={1:"snake",-1:"water",0:"gun"}

        you=youdict[youstr]

        print("Computer chose:",reversedict[computer])
        print("You Chose:",reversedict[you])

        if(computer==you):
                print("It's a DRAW")
        else:
                if(computer==-1 and you==0):
                                print("You lose")
                        
                elif(computer==-1 and you==1):
                                print("You win")
                        
                elif(computer==1 and you==-1):
                                print("You lose")
                        
                elif(computer==1 and you==0):
                                print("You win")
                        
                elif(computer==0 and you==1):
                                print("You lose")
                        
                elif(computer==0 and you==-1):
                                print("You win")
                        