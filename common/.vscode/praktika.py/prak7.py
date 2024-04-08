import tkinter as tk

def set_color(color):
    frame.config(background=color)

def set_size(size):
    root.geometry(size)

root = tk.Tk()
root.title("Ers")

frame = tk.Frame(root, width=200, height=200)
frame.pack()

menubar = tk.Menu(root)
root.config(menu=menubar)

color_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Red", command=lambda: set_color("red"))
color_menu.add_command(label="Green", command=lambda: set_color("green"))
color_menu.add_command(label="Blue", command=lambda: set_color("blue"))

size_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Size", menu=size_menu)
size_menu.add_command(label="500x500", command=lambda: set_size("500x500"))
size_menu.add_command(label="700x400", command=lambda: set_size("700x400"))

root.mainloop()



