import math


def calculate(expr):
    try:
        expr = expr.replace("x^y", "**")
        expr = expr.replace("sqrt", "math.sqrt")
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")

        return eval(expr, {"math": math})
    except Exception:
        return "Error"


