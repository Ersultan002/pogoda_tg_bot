import tkinter as tk

def hello():
    print("Hello ")

win = tk.Tk()
win.geometry("300x300")
win.title('Ers')

but = tk.Button(win, text = 'Hello',
                command=hello,
                ).pack()

win.mainloop()
