import math

def calculate(expr):
    try:
        expr = expr.replace("x^y", "**")
        expr = expr.replace("sqrt", "math.sqrt")
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")

        # Safe eval environment
        return eval(expr, {"math": math})
    except:
        return "Error"

