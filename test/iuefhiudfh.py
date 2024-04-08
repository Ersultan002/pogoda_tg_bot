import tkinter as tk

window=tk.Tk()
ROW= 10
COLUMNS=7

buttons = []
for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn= tk.Button(window, width=4, font='calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)
        
for row_btn in buttons:
    print(row_btn)

for i in range(ROW):
    for j in range(COLUMNS):
        btn= buttons[i][j]
        btn.grid(row=i, column=j)


window.mainloop()