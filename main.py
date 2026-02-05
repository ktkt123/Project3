import tkinter as tk
from engine import CalculatorEngine
from ui import CalculatorUI


def main():
    # Create main window
    root = tk.Tk()
    root.title("Simple Calculator")
    root.resizable(False, False)

    # Initialize engine and UI
    engine = CalculatorEngine()
    CalculatorUI(root, engine)

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
