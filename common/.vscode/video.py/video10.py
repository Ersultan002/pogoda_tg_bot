import tkinter as tk

def select_all():
    for check in [over_18 , commercial, follow ]:
        check.select()

def deselect_all():
    for check in [over_18 , commercial, follow ]:
        check.toggle()

def switch_all():
    for check in [over_18 , commercial, follow ]:
        check.deselect()

def Show():
    print('флажок 18', over_18_value.get())
    print('Реклама',  commercial_value.get())



win = tk.Tk()

over_18_value = tk.StringVar()
over_18_value.set('No')
commercial_value = tk.IntVar()
win.geometry("240x300+100+200")
win.title('Ers')

over_18 = tk.Checkbutton (win, text='Вам исполнтлось 18 лет?',
                         variable=over_18_value,
                         offvalue='No',
                         onvalue='Yes'
                         )



commercial = tk.Checkbutton(win, text='хотите получать рекламы ?',
                            variable=commercial_value,
                            offvalue=0,
                            onvalue=1
                           )
follow = tk.Checkbutton(win, text='Хотите подписаться на канал ?', indicatoron=0)
over_18.pack()
commercial.pack()
follow.pack()
tk.Button(win,text='select_all',command=select_all).pack()
tk.Button(win,text='deselect_all',command=deselect_all).pack()
tk.Button(win,text='switch_all',command=switch_all).pack()
tk.Button(win,text='Show',command=Show).pack()
win.mainloop()