from turtle import*
shape('turtle')
bgcolor('black')
colors=['cyan','pink','yellow','lime','purple','orange']
width(2)
for x in range(1,600,2):
    color(colors[x%6])
    forward(x)
    left(41)
