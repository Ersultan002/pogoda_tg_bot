from tkinter import *
root = Tk()
root.title('Ers')
canvas = Canvas(root, width=500, height=270, bg="gray")
for i in range(0, 5):
    row = i * 50
    for x in range(10, 490, 120):
        canvas.create_rectangle(x, row + 10, x + 120, row + 60, fill="white")
Massiv = [
    ["x", "y", "x and y", "x or y"],
    ["0", "0", "0", "0"],
    ["0", "1", "0", "1"],
    ["1", "0", "0", "1"],
    ["1", "1", "1", "1"]
]
RowX = 70
RowXi = -0.8
ColY = 25
ColYi = -0.5
for row in range(len(Massiv)):
    ColYi += 2
    RowXi = -0.8
    for col in range(len(Massiv[row])):
        RowXi += 1.75
        canvas.create_text(RowXi * RowX, ColYi * ColY,
        text=Massiv[row][col], justify=LEFT, font='10')
canvas.grid()
root.mainloop()
