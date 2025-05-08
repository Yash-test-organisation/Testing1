import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.expression = ""
        
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, width=400, height=50)
        input_frame.pack()

        input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), 
                               textvariable=self.input_text, width=30, bd=5, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        # Define buttons layout
        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'power'],
            ['1', '2', '3', '-', 'log'],
            ['0', '.', '=', '+', 'ln'],
            ['(', ')', 'sin', 'cos', 'tan'],
            ['C', 'factorial']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, item in enumerate(row):
                button = tk.Button(btns_frame, text=item, width=8, height=3, font=('arial', 12),
                                   command=lambda item=item: self.on_button_click(item))
                button.grid(row=row_index, column=col_index, padx=2, pady=2)

    def on_button_click(self, char):
        try:
            if char == '=':
                result = self.evaluate_expression(self.expression)
                self.input_text.set(result)
                self.expression = str(result)
            elif char == 'C':
                self.expression = ""
                self.input_text.set("")
            elif char == 'sqrt':
                self.expression = str(math.sqrt(eval(self.expression)))
                self.input_text.set(self.expression)
            elif char == 'power':
                self.expression += '**'
                self.input_text.set(self.expression)
            elif char == 'log':
                self.expression = str(math.log10(eval(self.expression)))
                self.input_text.set(self.expression)
            elif char == 'ln':
                self.expression = str(math.log(eval(self.expression)))
                self.input_text.set(self.expression)
            elif char == 'sin':
                self.expression = str(math.sin(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif char == 'cos':
                self.expression = str(math.cos(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif char == 'tan':
                self.expression = str(math.tan(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif char == 'factorial':
                x = eval(self.expression)
                if x < 0 or not float(x).is_integer():
                    raise ValueError("Factorial only defined for non-negative integers.")
                self.expression = str(math.factorial(int(x)))
                self.input_text.set(self.expression)
            else:
                self.expression += str(char)
                self.input_text.set(self.expression)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.expression = ""
            self.input_text.set("")

    def evaluate_expression(self, expression):
        return eval(expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
