import tkinter as tk

def resize_frame(width, height):
    frame.config(width=width, height=height)

root = tk.Tk()
root.title('Ers')
frame = tk.Frame(root, bg='red', width=200, height=200)
frame.pack()

btn1 = tk.Button(root, text="1", command=lambda: resize_frame(100, 100))
btn1.pack(side='left')

btn2 = tk.Button(root, text="2", command=lambda: resize_frame(200, 200))
btn2.pack(side='left')

btn3 = tk.Button(root, text="3", command=lambda: resize_frame(300, 300))
btn3.pack(side='left')

root.mainloop()

