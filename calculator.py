import sys
print(sys.path)

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

import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.result_display = QLineEdit()
        layout.addWidget(self.result_display)

        button_layout = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "/"],
            ["sqrt", "x^y", "sin", "cos", "tan"]
        ]

        for row in button_layout:
            row_widget = QWidget()
            row_layout = QHBoxLayout()
            row_widget.setLayout(row_layout)

            for label in row:
                button = QPushButton(label)
                button.clicked.connect(self.handle_button_click)
                row_layout.addWidget(button)

            layout.addWidget(row_widget)

        self.current_input = ""

    def handle_button_click(self):
        clicked_button = self.sender()
        clicked_text = clicked_button.text()

        if clicked_text == "=":
            try:
                result = self.calculate(self.current_input)
                self.result_display.setText(str(result))
                self.current_input = str(result)
            except Exception as e:
                self.result_display.setText("Error")
        elif clicked_text == "sqrt":
            try:
                result = self.calculate("sqrt(" + self.current_input + ")")
                self.result_display.setText(str(result))
                self.current_input = str(result)
            except Exception as e:
                self.result_display.setText("Error")
        else:
            self.current_input += clicked_text
            self.result_display.setText(self.current_input)

    def calculate(self, expression):
        try:
            return eval(expression)
        except Exception as e:
            return "Error"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator_app = CalculatorApp()
    calculator_app.show()
    sys.exit(app.exec_())
