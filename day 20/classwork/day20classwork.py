#making a function where it greets me
def greet():
    print("hello Sandro")

greet()

#igive mara ricxvebis jamit axla
def add():
    print(5+5+1)

add()

#kalkulatoris msgavsi
def add(num1,num2,operation):
    if operation == "+":
        print(num1+num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "*":
        print(num1*num2)
    elif operation == "/":
        print(num1/num2)
    else:
        print("error invalid operation")
add(3,2, "+")
add(15,9, "-")
add(8,8, "*")
add(30,15, "/")

#returnit
def add(num1,num2,operation):
    if operation == "+":
        return(num1+num2)
    elif operation == "-":
        return(num1-num2)
    elif operation == "*":
        return(num1*num2)
    elif operation == "/":
        return(num1/num2)
    else:
        return("error invalid operation")
add(3,2, "+")
add(15,9, "-")
add(8,8, "*")
add(30,15, "/")