import turtle 
import math

def draw_square():
    for x in range (4):
       turtle.forward(100)
       turtle.right (90)
       
def draw_circle():
    turtle.circle (50)
    
def draw_triangle():
    for x in range (3):
       turtle.forward (100)
       turtle.left(120)
       
choice = input ("Фигура танданыз (квадрат/шенбер/ушбурыш): ").lower()

turtle.speed(1) 

if choice == "квадрат":
    draw_square()
elif choice == "шенбер":
    draw_circle ()
elif choice == "ушбурыш" :
    draw_triangle()
else:
    print ("Дурыс емес! Тандаау жасаныз!!!!")
    turtle.done ()