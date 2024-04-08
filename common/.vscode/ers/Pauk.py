import turtle
num_legs = int (input ("Введите количество лап для паука: "))
turtle.circle (5)
for x in range (num_legs):
   turtle.forward (150)
   turtle.backward (150)
   turtle.left (360 / num_legs)
turtle.done ()