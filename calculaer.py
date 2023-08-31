import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.num1_label = tk.Label(root, text="Enter number 1:")
        self.num1_label.pack()

        self.num1_entry = tk.Entry(root , width=40)
        self.num1_entry.pack(pady=10)

        self.num2_label = tk.Label(root, text="Enter number 2:")
        self.num2_label.pack()

        self.num2_entry = tk.Entry(root, width=40)
        self.num2_entry.pack(pady=10)

        self.operation_label = tk.Label(root, text="Select operation:")
        self.operation_label.pack()

        self.operation_var = tk.StringVar()
        self.operation_var.set("+")

        self.operation_menu = tk.OptionMenu(root, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        operation = self.operation_var.get()

        if num1 and num2:
            try:
                num1 = float(num1)
                num2 = float(num2)
                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "*":
                    result = num1 * num2
                elif operation == "/":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        messagebox.showerror("Error", "Division by zero is not allowed.")
                        return
                self.result_label.config(text=f"Result: {result}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
        else:
            messagebox.showerror("Error", "Please enter both numbers.")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

