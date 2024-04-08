import tkinter as tk

win = tk.Tk()

win.geometry(f"300x400+100+200")
win.title('Ers')

label_1 = tk.Label(win, text='Hello',
                  bg='blue',
                  fg='white',
                  font=('Arial!',15,'bold'),
                  padx=20,
                  pady=40,
                  width=20,
                  height=10,
                  anchor='sw',
                  relief=tk.RAISED,
                  bd=10,
                  justify=tk.LEFT
                  )
label_1.pack()
win.mainloop()