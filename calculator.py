def sum (a, b):
    return a + b

def rest(a, b):
    return a - b


def multiplication (a, b):
    return a * b


def divition (a, b):
    return a / b

while True:
    try:
        print("This is a basic calculator using Python")
        a = int(input("Introduce the first number: "))
        b = int(input("Introduce the second number: "))
        option = int(input(" - 1. Sum \n - 2. Rest \n - 3. Multiplication \n - 4. Divition \n Select the function: "))

        if option == 1:
            print(f"The sum of {a} + {b} is {sum(a,b)}")
            break
        
        elif option == 2:
            print(f"The rest of {a} - {b} is {rest(a,b)}")
            break
        
        elif option == 3:
            print(f"The multiplication of {a} * {b} is {multiplication(a,b)}")
            break
        
        elif option == 4:
            if b == 0:
                print(f"The divition of {a} / 1 is {divition(a,b)}")
                break
            else:
                print(f"The divition of {a} / {b} is {divition(a,b)}")
                break
        else:
            print("Select a correct function \n")
            
    except ValueError:
        print("Incorrect value. \n")
    except ZeroDivisionError:
        print("We can not divide by 0. Please try again \n")
    
        
        