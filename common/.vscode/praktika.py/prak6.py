import tkinter as tk

def update_label(event):
    if event.num == 1:
        checked = [var.get() for var, chk in zip(vars, chks) if chk.get() == 1]
        label.config(text='Tandalgandar: ' + ', '.join(checked))
    elif event.num == 3:
        unchecked = [var.get() for var, chk in zip(vars, chks) if chk.get() == 0]
        label.config(text='Tandalmagandar: ' + ', '.join(unchecked))

root = tk.Tk()
root.title('Ers')
root.geometry("300x300")

vars = []
chks = []
for i in range(3):
    var = tk.StringVar(value=f'Checkbox {i+1}')
    chk_state = tk.IntVar()
    chk = tk.Checkbutton(root, text=f'Checkbox {i+1}', variable=chk_state, onvalue=1, offvalue=0)
    chk.pack()
    vars.append(var)
    chks.append(chk_state)

label = tk.Label(root, text="", width=40, font=15)
label.bind('<Button-1>', update_label)
label.bind('<Button-3>', update_label)
label.pack()

root.mainloop()
