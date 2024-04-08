import tkinter as tk

def update_label(event):
    label.config(text=entry.get())

root = tk.Tk()
root.title('Ers')
root.geometry("300x300")

entry = tk.Entry(root)
entry.bind('<Return>', update_label)
entry.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
