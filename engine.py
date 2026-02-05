import math  

class CalculatorEngine:
    def evaluate(self, expr):
        # Remove leading and trailing spaces
        expr = expr.strip()
        if expr == "":
            raise ValueError("It's empty")

        # Convert common calculator symbols to Python operators
        expr = expr.replace("×", "*").replace("÷", "/")

        # Disable built-in functions and provide an empty safe environment
        env = {}
        return eval(expr, {"__builtins__": {}}, env)
