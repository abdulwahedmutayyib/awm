from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from logic import calculate   # import logic engine

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
                multiline=False, readonly=True, halign="right", font_size=55
                )
        main_layout.add_widget(self.solution)
        buttons = [
                ["7", "8", "9", "/"],
                ["4", "5", "6", "*"],
                ["1", "2", "3", "-"],
                [".", "0", "C", "+"],
                ["sqrt", "x^y", "sin", "cos", "tan"],
                ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                        text=label,
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                        )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equals_button = Button(
                text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
    button_text = instance.text

    if button_text == "C":
        self.solution.text = ""

    elif button_text in ["sqrt", "sin", "cos", "tan"]:
        # append function format: sqrt( , sin( , etc
        self.solution.text = current + f"{button_text}("

    elif button_text == "x^y":
        # replace with power operator
        self.solution.text = current + "x^y"

    else:
        if current and (self.last_was_operator and button_text in self.operators):
            return
        elif current == "0" and button_text in self.operators:
            return
        else:
            self.solution.text = current + button_text

    self.last_button = button_text
    self.last_was_operator = self.last_button in self.operators


    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = self.calculate(text)
            self.solution.text = str(solution)


    def calculate(self, expression):
        return calculate(expression)


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
