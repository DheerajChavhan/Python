a=90

def fun():
    global a         # It will change value of a outside the function 
    a=3
    print(a)

fun()
print(a)