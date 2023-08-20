import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid input"

def exponentiation(x, y):
    return x ** y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Exit")

    choice = input("Enter choice (1-10): ")

    if choice == '10':
        print("Calculator exiting...")
        break

    if choice in ['1', '2', '3', '4', '6', '7', '8', '9']:
        num1 = float(input("Enter first number: "))
    
    if choice in ['1', '2', '3', '4', '6']:
        num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", square_root(num1))
    elif choice == '6':
        print("Result:", exponentiation(num1, num2))
    elif choice == '7':
        print("Result:", sine(num1))
    elif choice == '8':
        print("Result:", cosine(num1))
    elif choice == '9':
        print("Result:", tangent(num1))
    else:
        print("Invalid input")

