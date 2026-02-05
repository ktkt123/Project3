import math  # Import Python's built-in math module (sin, cos, tan, sqrt, pi, e)

class CalculatorEngine:
    """
    CalculatorEngine:
    - Supports basic expression evaluation using eval()
    - Supports scientific functions: sin, cos, tan, sqrt
    - Supports DEG/RAD mode for trigonometric functions
    """

    def __init__(self):
        # Angle mode setting:
        # True  -> DEG (input angles are treated as degrees)
        # False -> RAD (input angles are treated as radians)
        self.deg_mode = True

    def set_deg_mode(self, deg_mode):
        """
        Set angle mode.
        deg_mode = True  -> DEG mode
        deg_mode = False -> RAD mode
        """
        self.deg_mode = deg_mode

    def _to_rad(self, x):
        """
        Convert input angle to radians if currently in DEG mode.
        If already in RAD mode, return the input unchanged.
        """
        if self.deg_mode:
            return math.radians(x)  # degrees -> radians
        return x  # already radians

    # -----------------------------
    # Functions exposed to eval()
    # -----------------------------
    def sin(self, x):
        """Sine function (uses DEG/RAD mode)."""
        return math.sin(self._to_rad(x))

    def cos(self, x):
        """Cosine function (uses DEG/RAD mode)."""
        return math.cos(self._to_rad(x))

    def tan(self,x):
        """Tangent function (uses DEG/RAD mode)."""
        return math.tan(self._to_rad(x))

    def sqrt(self, x):
        """Square root function."""
        return math.sqrt(x)

    # -----------------------------
    # Main evaluation method
    # -----------------------------
    def evaluate(self, expr):
        """
        Evaluate a calculator expression string and return the result as float.

        Examples of supported inputs:
        - "1 + 2 * 3"
        - "sin(30)"   (DEG mode)
        - "√9"        (will be converted to sqrt(9))
        - "2^3"       (will be converted to 2**3)
        - "pi * 2"
        """
        # Remove leading/trailing whitespace
        expr = expr.strip()

        # Reject empty input
        if expr == "":
            raise ValueError("It's empty")

        # Convert calculator symbols to Python syntax:
        # ^  -> **  (power)
        # ×  -> *   (multiply)
        # ÷  -> /   (divide)
        # √  -> sqrt (square root function name)
        expr = expr.replace("^", "**")
        expr = expr.replace("×", "*")
        expr = expr.replace("÷", "/")
        expr = expr.replace("√", "sqrt")

        # Safe environment for eval():
        # Only expose the functions/constants we want to allow.
        env = {
            "sin": self.sin,
            "cos": self.cos,
            "tan": self.tan,
            "sqrt": self.sqrt,
            "pi": math.pi,  # constant π
            "e": math.e,    # constant e
        }

        # Evaluate with builtins disabled to reduce risk
        result = eval(expr, {"__builtins__": {}}, env)

        # Force float output (e.g., int -> float)
        return float(result)
