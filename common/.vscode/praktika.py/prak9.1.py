from tkinter import *
root = Tk()
root.title('Ers')
canvas = Canvas(root, width=500, height=320, bg="lightgray")
canvas.create_rectangle(5, 5, 500, 320, width=5, outline="blue", fill="white")
squareX = 250
squareY = 40
for y in range(0,11):
    canvas.create_rectangle([squareX, squareY+(y*20)], [squareX+20,squareY+((y+1)*20)],
    fill="yellow")
    y += 1
canvas.create_rectangle(150, 40, 170, 120, fill="lime")
canvas.create_rectangle(350, 40, 370, 160, fill="lightblue")
canvas.create_line(270, 110, 310, 110, width=3)
canvas.create_line(310, 112, 310, 50, width=3)
canvas.create_line(309, 50, 350, 50, width=3, arrow=LAST)
canvas.create_line(250, 70, 200, 70, width=3)
canvas.create_line(200, 72, 200, 50, width=3)
canvas.create_line(202, 50, 170, 50, width=3, arrow=LAST)
canvas.create_line(250, 210, 90, 210, width=3)
canvas.create_line(90, 212, 90, 50, width=3)
canvas.create_line(90, 50, 150, 50, width=3, arrow=LAST)
canvas.create_text(150, 40, text="F1", anchor="sw", font='20')
canvas.create_text(255, 40, text="P", anchor="sw", font='20')
canvas.create_text(350, 40, text="F2", anchor="sw", font='20')
canvas.create_text(310, 280,
text="P - main program\nF1 - function 1\nF2 - function 2",
anchor="sw", font='20')
canvas.grid()
root.mainloop()
