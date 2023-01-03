import os              
from art import logo

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

operations ={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division,
}

exit='n'
continue_='n'
while continue_=='n':
    os.system('clear')
    print(logo)
    num1 =int (input ("Enter your first number : "))
    continue_='y'
    while continue_=='y':
        for symbol in operations:
            print(symbol)
        operation = input ("Pick an operation : ")
        num2 =int (input ("Enter your second number : "))
        function = operations[operation]
        print(f"{num1} {operation} {num2} = {function(num1,num2)}")
        num1=function(num1,num2)        
        exit=input("If you want to close the calculator type 'y' otherwise type anythingggg :  ")
        if exit=='y':
            print("POWER OFF!!!")
            quit()
        continue_=input(f"Type 'y' if you want to continue with the '{num1}' ,type 'n' for new calculation :  ")
    





