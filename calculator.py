
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

import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        operation = operation_var.get()
        
        if operation == "Add":
            result = add(x, y)
        elif operation == "Subtract":
            result = subtract(x, y)
        elif operation == "Multiply":
            result = multiply(x, y)
        elif operation == "Divide":
            result = divide(x, y)
        elif operation == "Square Root":
            result = square_root(x)
        elif operation == "Exponentiation":
            result = exponentiation(x, y)
        elif operation == "Sine":
            result = sine(x)
        elif operation == "Cosine":
            result = cosine(x)
        elif operation == "Tangent":
            result = tangent(x)
        else:
            result = "Invalid operation"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Create input fields
entry_x = tk.Entry(app, width=10)
entry_y = tk.Entry(app, width=10)

# Create operation dropdown
operations = ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Exponentiation", "Sine", "Cosine", "Tangent"]
operation_var = tk.StringVar()
operation_var.set(operations[0])  # Default operation
operation_menu = tk.OptionMenu(app, operation_var, *operations)

# Create calculate button
calculate_button = tk.Button(app, text="Calculate", command=calculate)

# Create result label
result_label = tk.Label(app, text="Result: ")

# Layout widgets
entry_x.pack()
entry_y.pack()
operation_menu.pack()
calculate_button.pack()
result_label.pack()

# Start the GUI main loop
app.mainloop()
