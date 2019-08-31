import turtle as t
from turtle import Turtle, Screen
import time
t.title("windows update")
wn = t.Screen()
wn.bgcolor("#427af4")
#border
border = t.Turtle()
border.color("white")
border.penup()
border.bk(300)
border.pendown()
for x in range(2):
    border.fd(600)
    border.lt(90)
    border.fd(50)
    border.lt(90)
border.ht()

border_x = border.xcor()
border_y = border.ycor()

#the text
text = t.Turtle()
text.penup()
text.ht()
text.lt(90)
text.fd(100)
text.lt(90)
text.fd(100)
text.rt(180)
text.pendown()
text.write("Working on updates", font = ("Arial",14))

#the text 2
text1 = t.Turtle()
text1.penup()
text1.ht()
text1.lt(90)
text1.fd(70)
text1.lt(90)
text1.fd(125)
text1.rt(180)
text1.pendown()
text1.write("Don't turn off your computer", font = ("Arial",14))

#the load line
load = t.Turtle()
load.color("white")
load.goto(border_x,border_y)
load.ht()

load_width = 0

while load_width < 600:
    load.begin_fill()
    time.sleep(1)
    load.fd(load_width)
    load.lt(90)
    load.fd(50)
    load.lt(90)
    load.fd(load_width)
    load.lt(90)
    load.fd(50)
    load.lt(90)
    load.end_fill()
    load_width += 1

if load_width == 600:
    time.sleep(2)
    t.bye()
    print("update complete")














    
