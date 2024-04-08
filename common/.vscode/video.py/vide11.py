import tkinter as tk


levels ={
    1: 'Easy',
    2: 'Middle',
    3: 'Hard'

}

def select_level():
    level = level_var.get()
    level_text.set(f"вы выбрали{ level} уровень")
    print(levels[level])
win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('Ers')

level_var=tk.IntVar()
nation_var=tk.IntVar()
level_text = tk.StringVar()

tk.Label(win, text='Выберите уровень сложности').pack()
for level in sorted(levels):

 tk.Radiobutton(win, text=levels[level], variable=level_var, value=level, command=select_level).pack()
tk.Label(win,textvariable=level_text).pack()


win.mainloop()


