from tkinter import *

def moveObject():
    if c.coords(sq)[2] < 300:
        c.move(sq, 1, 0)
    if c.coords(sq)[3] < 200:
        c.move(sq, 0, 1)
    root.after(30, moveObject)

root = Tk()
root.title('Ers')
c = Canvas(width=460,height=460)
c.pack()
sq = c.create_rectangle(0,0,20,20, fill="darkgreen")
moveObject()
root.mainloop()
