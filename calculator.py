
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

# Now, let's create a test case using the unittest framework

import unittest

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    # Add more test methods for other functions

if __name__ == '__main__':
    unittest.main()
    import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Complex Calculator")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        button_layout = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "/"]
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
                result = eval(self.current_input)
                self.input_field.setText(str(result))
                self.current_input = str(result)
            except Exception as e:
                self.input_field.setText("Error")
        else:
            self.current_input += clicked_text
            self.input_field.setText(self.current_input)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    calc_app.show()
    sys.exit(app.exec_())



