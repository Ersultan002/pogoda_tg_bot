import tkinter as tk

def resize(event):
    if event.keysym == 'space':
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            frame.config(width=width, height=height)
        except ValueError:
            pass

root = tk.Tk()
root.title('Ers')

width_entry = tk.Entry(root)
width_entry.pack()

height_entry = tk.Entry(root)
height_entry.pack()

frame = tk.Frame(root, width=200, height=200, bg='yellow')
frame.pack()

root.bind('<Key>', resize)

root.mainloop()

