import tkinter as tk
from tkinter import ttk

def update_color(val):
    color = f'#{int(float(val)):02x}{int(float(val)):02x}{int(float(val)):02x}'
    frame.config(background=color)

root = tk.Tk()
root.title("Ers")

frame = tk.Frame(root, width=200, height=200)
frame.pack()

scale = ttk.Scale(root, from_=0, to=255, command=update_color)
scale.pack()

root.mainloop()
