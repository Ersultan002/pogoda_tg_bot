import tkinter as tk
from tkinter import ttk

def get_print():
    print(ent.get())
    print(ent2.get())

win = tk.Tk()
win.geometry("400x300")
win.title('Ers')
win['bg'] = 'green'


lab = tk.Label(win, text='Ваш адрес: ', bg='blue').pack()
ent = tk.Entry(win, bg='white')
ent.pack()

lab2 = tk.Label(win, text='Комментарий: ', bg='pink').pack()
ent2 = tk.Entry(win,
                width=30,
                )
ent2.pack(padx=30, ipady=30)

but = tk.Button(win, text='Отправить', 
                bg='yellow', command=get_print,
                ).pack()

win.mainloop()
