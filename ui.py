import tkinter as tk
from tkinter import messagebox

class CalculatorUI:
    def __init__(self, root, engine):
        self.root = root
        self.engine = engine

        # Entry widget to display the current expression and result
        self.display = tk.Entry(root, font=("Arial", 15), justify="right", width=20)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Button layout for basic arithmetic operations
        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0",".","=","+"],
            ["("," )","C","⌫"],
        ]

        # Create buttons dynamically
        for i in range(len(buttons)):
            for j in range(4):
                text = buttons[i][j]
                temp = tk.Button(root, text=text, width=5, height=2, command=self.make_cmd(text))
                temp.grid(row=i+1, column=j, padx=5, pady=5)

    # Create a command function for each button
    def make_cmd(self, text):
        def cmd():
            if text == "=":
                self.calculate()
            elif text == "C":
                self.clear()
            elif text == "⌫":
                self.backspace()
            else:
                self.append(text)
        return cmd

    # Get current text from display
    def get(self):
        return self.display.get()

    # Set text in display
    def set(self, s):
        self.display.delete(0, tk.END)
        self.display.insert(0, s)

    # Append a character to the display
    def append(self, s):
        self.set(self.get() + s)

    # Clear the display
    def clear(self):
        self.set("")

    # Remove the last character
    def backspace(self):
        s = self.get()
        self.set(s[:-1])

    # Perform the calculation
    def calculate(self):
        try:
            result = self.engine.evaluate(self.get())
            self.set(str(result))
        except:
            self.set("Error")
