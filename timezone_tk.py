# import tkinter as tk
# from time import strftime

# def time():
#     string = strftime('%H:%M:%S %p')
#     label.config(text=string)
#     label.after(1000, time)

# root = tk.Tk()
# root.title("Horloge")
# label = tk.Label(root, font=('calibri', 40, 'bold'),text="Time zone" , background='purple', foreground='white')
# label.pack(anchor='center')

# label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
# label.pack(anchor='center')


# time()

# root.mainloop()
# Variable = 1_000_000
# print(Variable)
# def digitize(n):
#     return [int(x) for x in str(n)[::-1]]
# print(digitize(32134627890))
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
def is_isogram(string):
    string = string.lower()
    return all(string.count(c) == 1 for c in string)
print(all("string".count(c) == 1 for c in "string"))