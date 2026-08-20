import functions

while True:
    try:
        print("This is a basic calculator using Python")
        a = int(input("Introduce the first number: "))
        b = int(input("Introduce the second number: "))
        option = int(input(" - 1. Sum \n - 2. Rest \n - 3. Multiplication \n - 4. Divition \n - 5. Module \n Select the function: "))

        if option == 1:
            print(f"The sum of {a} + {b} is {functions.sum(a,b)}")
            break
        
        elif option == 2:
            print(f"The rest of {a} - {b} is {functions.rest(a,b)}")
            break
        
        elif option == 3:
            print(f"The multiplication of {a} * {b} is {functions.multiplication(a,b)}")
            break
        
        elif option == 4:
            print(f"The divition of {a} / {b} is {functions.divition(a,b)}")
            break
        
        elif option == 5:
            print(f"The module of {a} % {b} is {functions.module(a,b)}")
            break
        else:
            print("Select a correct function \n")
            
    except ValueError:
        print("Incorrect value. \n")
    except ZeroDivisionError:
        print("We can not divide by 0. Please try again \n")
    
        
        