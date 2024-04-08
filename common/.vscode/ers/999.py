from turtle import*
shape('turtle')
bgcolor('black')
colors=['green','orange','red','pink','blue','yellow']
width(2)
for x in range(5,400,2):
    color(colors[x%6])
    forward(x)
    left(61)
