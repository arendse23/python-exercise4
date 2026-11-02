
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

import math_operations
while True:
    print("\n--simple calculator--")
    print("select operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    choice = input("Enter choice (1\2\3\4): ")

    if choice == '5':
        print("Exiting the calculator.")
        break

    if choice in ('1','2','3','4'):
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", math_operations.add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", math_operations.subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", math_operations.multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", math_operations.divide(num1,num2))
    else:
        print("invalid input")