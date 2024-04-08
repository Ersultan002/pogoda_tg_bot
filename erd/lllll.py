

def say_hello():
    print('helle')

def add_label():
    label = tk.Label(win,text='new')
    label.pack()

def counter():
    global count
    count+=1
    btn4['text'] = f'Счетчик:  {count}'


count=0
    

import tkinter as tk

win = tk.Tk()

win.geometry(f"400x500+100+200")    
win.title('Ers')

btn1 = tk.Button(win,text='Hello',
                 command=say_hello)
btn2 = tk.Button(win,text='add_label',
                 command=add_label)
btn3 = tk.Button(win,text='lambda',
                 command=lambda: tk.Label(win,text='new labda').pack())
btn4 = tk.Button(win,text='счетчик:{count} ',
                 command=counter,
                 bg='red')
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
win.mainloop()