from tkinter import *
root=Tk()
c1=IntVar()
c2=IntVar()
c3=IntVar()
c4=IntVar()
c5=IntVar()
che1=Checkbutton(root,text="1",
   variable=c1,onvalue=1,offvalue=0)
che2=Checkbutton(root,text="2",
   variable=c2,onvalue=1,offvalue=0)
che3=Checkbutton(root,text="3",
   variable=c3,onvalue=1,offvalue=0)
che4=Checkbutton(root,text="4",
   variable=c4,onvalue=1,offvalue=0)
che5=Checkbutton(root,text="5",
   variable=c5,onvalue=1,offvalue=0)
tx=Text(root,height=10,width=15)
def clk1(event):
 if che1=="1":
  tx.delete(1.0,END)
  tx.insert(END,"выбран флажок #1 /n")
if che2=="1":
 tx.delete(1.0,END)
 tx.insert(END,"выбран флажок #2 /n")
if che3=="1":
 tx.delete(1.0,END)
 tx.insert(END,"выбран флажок #3 /n") 
if che4=="1":
 tx.delete(1.0,END)
 tx.insert(END,"выбран флажок #4 /n")
if che5=="1":
 tx.delete(1.0,END)
 tx.insert(END,"выбран флажок #5 /n")

def clk3(event):
 if che1=="0":
  tx.delete(1.0,END)
 tx.insert(END,"флажок #1 не был выбран /n")
if che1=="0":
 tx.delete(1.0,END)
 tx.insert(END,"флажок #1 не был выбран /n")
if che2=="0":
 tx.delete(1.0,END)
 tx.insert(END,"флажок #2 не был выбран /n")
if che3=="0":
 tx.delete(1.0,END)
 tx.insert(END,"флажок #3 не был выбран /n")
if che4=="0":
 tx.delete(1.0,END)
 tx.insert(END,"флажок #4 не был выбран /n")
if che5=="0":
 tx.delete(1.0,END)
 tx.insert(END,"флажок #5 не был выбран /n")
 tx.pack()
 che1.pack()
 tx.bind("<Button-1>",clk1)
 tx.bind("<Button-3>",clk3)
 root.mainloop()