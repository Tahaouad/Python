import tkinter as tk

def button_click(number):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current + str(number))

def clear():
    screen.delete(0, tk.END)

def calculate():
    expression = screen.get()
    try:
        result = eval(expression)
        screen.delete(0, tk.END)
        screen.insert(0, result)
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Erreur")

root = tk.Tk()
root.title("Calculatrice Simple")
root.geometry("400x500")  
screen = tk.Entry(root, font=("Arial", 24), width=10)
screen.grid(row=0, column=0, columnspan=4)

button_color = 'orange'

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'  
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate, bg=button_color, font=("Arial", 18)).grid(row=row_val, column=col_val, padx=10, pady=10)
    elif button == 'C':
        tk.Button(root, text=button, command=clear, bg=button_color, font=("Arial", 18)).grid(row=row_val, column=col_val, padx=10, pady=10)
    else:
        tk.Button(root, text=button, command=lambda b=button: button_click(b), bg=button_color, font=("Arial", 18)).grid(row=row_val, column=col_val, padx=10, pady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
