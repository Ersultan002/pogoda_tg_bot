import tkinter as tk

win = tk.Tk()
win.geometry("500x500")
win.title('Ers')

fra = tk.Frame(win,width=300,height=200,bg="green",bd=20)
fra.pack()

sca = tk.Scale(fra, orient='horizontal', 
                length=300, from_=0, to=200,
                tickinterval=10, resolution=5
                ).pack()

w = tk.Toplevel(win, relief='sunken', bd=10, bg="lightblue")
w.title('2 tereze')
w.minsize(width=400, height=200)

txq = tk.Text(w, width=40, height=3, font='14')
scrq = tk.Scrollbar(w, command=txq.yview)
txq.configure(yscrollcommand=scrq.set)

txq.grid(row=0, column=0)
scrq.grid(row=0, column=1)

win.mainloop()
