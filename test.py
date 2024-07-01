# test_calculator.py

import pytest
from calculator import CalculatorApp  # assuming the code is in calculator.py

@pytest.fixture
def app():
    return CalculatorApp()

def test_build(app):
    # Test that the build method returns a BoxLayout
    assert isinstance(app.build(), BoxLayout)

def test_on_button_press(app, monkeypatch):
    # Test that the on_button_press method updates the solution text
    app.solution.text = "10"
    button = Button(text="+")
    app.on_button_press(button)
    assert app.solution.text == "10+"

    # Test that the on_button_press method clears the solution text when "C" is pressed
    app.solution.text = "10+20"
    button = Button(text="C")
    app.on_button_press(button)
    assert app.solution.text == ""

    # Test that the on_button_press method doesn't add an operator if the last button was an operator
    app.solution.text = "10+"
    button = Button(text="-")
    app.on_button_press(button)
    assert app.solution.text == "10+"

    # Test that the on_button_press method doesn't add an operator if the current text is "0"
    app.solution.text = "0"
    button = Button(text="+")
    app.on_button_press(button)
    assert app.solution.text == "0"

def test_on_solution(app, monkeypatch):
    # Test that the on_solution method calculates the solution correctly
    app.solution.text = "10+20"
    button = Button(text="=")
    app.on_solution(button)
    assert app.solution.text == "30"

    # Test that the on_solution method handles errors correctly
    app.solution.text = "10/0"
    button = Button(text="=")
    app.on_solution(button)
    assert app.solution.text == "Error"

def test_calculate(app):
    # Test that the calculate method evaluates the expression correctly
    assert app.calculate("10+20") == 30

    # Test that the calculate method handles errors correctly
    assert app.calculate("10/0") == "Error"
