# Calculator With History
HISTORY_FILE = "History.txt"

def show_History():
    file=open(HISTORY_FILE,'r')
    lines=file.readlines()
    if len(lines)==0:
        print("NO HISTORY FOUND!!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(HISTORY_FILE,'w')
    file.close()
    print("HISTORY CLEARED!!")

def save_to_history(equation,result):
    file=open(HISTORY_FILE,'a')
    file.write(equation +" "+ "=" +" "+ str(result) + "\n")
    file.close()

def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("INVALID INPUT")
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op == "+":
        result = num1 + num2
    
    elif op == "*":
        result = num1 * num2
    
    elif op == "**":
        result = num1**num2
    
    elif op == "-":
        result = num1-num2
    
    elif op == "/":
        if num2==0:
            print("CANNOT DIVIDE BY 0")
            return
        result = num1/num2
    else:
        print("INVALID OPERATOR")  

    if int(result)==result:
        result=int(result)
    print("Result:",result)
    save_to_history(user_input,result)

def main():
    print("SIMPLE CALCULATOR (type History ,clear,exit)\n")        
    while True:
            user_input=input("Enter Calculation(+,-,*,/,**) OR Command(history ,clear,exit)\n")    
            if(user_input=="exit"):
                print("Good Bye, Thank You for using the Calculator!")
                break
            elif user_input=="history":
                show_History()
            elif user_input=="clear":
                clear_history()
            else:
                calculate(user_input)

main()
            
            
    






