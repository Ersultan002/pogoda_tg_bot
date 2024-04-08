from turtle import*
shape('turtle')
speed(0)
bgcolor('black')
colors=['cyan','pink','yellow','lime','purple','orange']
width(2)
for x in range(1,10000,8):
    color(colors[x%6])
    forward(x)
    left(121)
