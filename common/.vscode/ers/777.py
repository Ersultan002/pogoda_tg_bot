from turtle import*
shape('turtle')
speed(0)
bgcolor('black')
colors=['cyan','pink','yellow','lime']
width(2)
for x in range(1,400,5):
    color(colors[x%4])
    forward(x)
    left(91)