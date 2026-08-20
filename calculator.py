import functions

while True:
    try:
        print("This is a basic calculator using Python")
        a = int(input("Introduce the first number: "))
        b = int(input("Introduce the second number: "))
        option = int(input(" - 1. Sum \n - 2. Rest \n - 3. Multiplication \n - 4. Divition \n - 5. Module \n Select the function: "))

        operators = {
            1: functions.add,
            2: functions.substract,
            3: functions.multiplication,
            4: functions.division,
            5: functions.modulo,
        }
        if option in operators:
            print(operators[option](a,b))
            break

        else:
            print("Select a correct function \n")
            
    except ValueError:
        print("Incorrect value. \n")
    except ZeroDivisionError:
        print("We can not divide by 0. Please try again \n")
    
        
        