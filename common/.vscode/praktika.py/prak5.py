import tkinter as tk
from tkinter import messagebox

def show_values(event):
    values = [var.get() for var in vars]
    if event.num == 1:
        messagebox.showinfo("Tandalgandar", ", ".join([name for name, value in zip(names, values) if value]))
    elif event.num == 3:
        messagebox.showinfo("Tandalmagandar", ", ".join([name for name, value in zip(names, values) if not value]))

root = tk.Tk()
root.title('Ers')

names = ["Флажок 1", "Флажок 2", "Флажок 3"]
vars = [tk.BooleanVar() for _ in names]

for name, var in zip(names, vars):
    chk = tk.Checkbutton(root, text=name, variable=var)
    chk.pack()

text = tk.Text(root)
text.bind("<Button-1>", show_values)
text.bind("<Button-3>", show_values)
text.pack()

root.mainloop()
