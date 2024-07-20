import tkinter as tk
from tkinter import ttk

def calculator():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = combo_operator.get()
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        entry_result.delete(0,tk.END)
        entry_result.insert(0, result)

    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Invalid input")
        

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = ttk.Label(root, text="Number1: ")
label_num1.grid(row=0, column=0,padx=10, pady=10)
entry_num1 = ttk.Entry(root, width=15)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_operator = ttk.Label(root, text="Operator: ")
label_operator.grid(row=0, column=2, padx=10, pady=10)
combo_operator = ttk.Combobox(root, values=['+', '-', '*', '/'],width=5)
combo_operator.grid(row=0, column=3, padx=10, pady=10)
combo_operator.current(0)

label_num2 = ttk.Label(root, text="Number2: ")
label_num2.grid(row=0, column=4,padx=10, pady=10)
entry_num2 = ttk.Entry(root, width=15)
entry_num2.grid(row=0, column=5, padx=10, pady=10)

btn_calculator = ttk.Button(root, text="Calculate", command=calculator)
btn_calculator.grid(row=1, columnspan=6, padx=10, pady=10)

label_result = ttk.Label(root, text="Result: ")
label_result.grid(row=2, column=0, padx=10, pady=10)
entry_result = ttk.Entry(root, width=30)
entry_result.grid(row=2, column=1, columnspan=5, padx=10, pady=10)

root.mainloop()











   