from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

def erase():
    tx.delete('3.0', '4.0')

def smiley(event):
    cv = Canvas(height=30,width=30)
    cv.create_oval(1,1,29,29,fill="yellow")
    cv.create_oval(9,10,12,12)
    cv.create_oval(19,10,22,12)
    cv.create_polygon(9,20,15,24,22,20)
    tx.window_create(CURRENT,window=cv)

root = Tk()
root.title('Ers')

tx = Text(font=('times',12),width=50,height=15,wrap=WORD)
tx.pack(expand=YES,fill=BOTH)
tx.insert(1.0,'Дзэн Питона\n '
              ' Если интерпретатору Питона дать команду\n '
              ' import this ("импортировать это"),\n '
              ' то выведется так называемый "Дзен Питона".\n Некоторые выражения:\n '
              ' * Если реализацию сложно объяснить — это плохая идея.\n '
              ' * Ошибки никогда не должны замалчиваться.\n\
                * Явное лучше неявного.\n\n')

tx.tag_add('title','1.0','1.end')
tx.tag_add('special','6.0','8.end')
tx.tag_add('special','3.0','3.11')

tx.tag_config('title',foreground='red',
              font=('times',14,'underline'),justify=CENTER)
tx.tag_config('special',background='grey85',font=('Dejavu',10,'bold'))

bt = Button(tx,text='Стереть',command=erase)
tx.window_create(END,window=bt)

tx.tag_add('my_tag', '1.0', END)
tx.tag_config('my_tag', font=('Helvetica', '16'))

tx.bind('<Button-1>',smiley)

root.mainloop()
