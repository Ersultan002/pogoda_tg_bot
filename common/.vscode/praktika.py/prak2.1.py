import tkinter as tk
dana = {
    1:'0-10' ,
    2:'11-20' ,
    3:'21-30' ,
    4: '31-40' ,
}
tuster = {
    1:'Red' , 
    2:'Blue' ,
    3:'Green' ,
    4: 'Yellow'
}
def select_dana():
    danalar = dana_var.get()
    dana_text.set(f"Siz tandagan qatar : {danalar}")
    print(dana[danalar])

def select_tus():
    tus = tus_text.get()
    print(tus)

win = tk.Tk()
win.geometry("400x300")
win.title('Ers')
win['bg'] = 'blue'

dana_var = tk.IntVar()
dana_text = tk.StringVar()
tus_var = tk.IntVar()
tus_text = tk.StringVar()

text = tk.Label(win, text = 'Сколько штук: ').pack()
for danalar in sorted(dana):
    tk.Radiobutton(win, text = dana[danalar], variable=dana_var, value=danalar, command=select_dana).pack()
tk.Label(win, textvariable=dana_text).pack()

text = tk.Label(win, text = 'Какого цвета: ').pack()
tk.Radiobutton(win, text = 'red', variable=tus_var, value=1, command=select_tus, bg='red').pack()
tk.Radiobutton(win, text = 'blue', variable=tus_var, value=2, command=select_tus, bg='blue').pack()
tk.Radiobutton(win, text = 'green', variable=tus_var, value=3, command=select_tus, bg='green').pack()
tk.Radiobutton(win, text = 'yellow', variable=tus_var, value=4, command=select_tus, bg='yellow').pack()

win.mainloop()
