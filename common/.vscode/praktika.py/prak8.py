from tkinter import *
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *

def _open():
    text1.delete(1.0, END)
    op = askopenfilename()
    for i in fileinput.input(op):
        text1.insert(END, i)

def _save():
    sa = asksaveasfilename()
    letter = text1.get(1.0, END)
    f = open(sa, "w")
    f.write(letter)
    f.close()

def close_win():
    if askyesno("Выход", "Сохранить или нет?"):
        _save()
    else:
        root.destroy()

def about():
    showinfo("Текстовый редактор",
             "Это текстовый редактор.\n(тестовая версия)")

root = Tk()

mainMenu = Menu(root)
root.config(menu=mainMenu)

menuFile = Menu(mainMenu)
mainMenu.add_cascade(label="Файл", menu=menuFile)
menuFile.add_command(label="Открыть...", command=_open)
menuFile.add_command(label="Сохранить как...", command=_save)
menuFile.add_command(label="Выход", command=close_win)

menuHelp = Menu(mainMenu)
mainMenu.add_cascade(label="Помощь", menu=menuHelp)
menuHelp.add_command(label="О программе", command=about)

text1 = Text(root, width=40, height=15, font="12")
text1.pack()

root.mainloop()
