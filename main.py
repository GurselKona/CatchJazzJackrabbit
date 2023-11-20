import random
import turtle
import time

score = 0
timer = 10


def is_catch(x, y):
    tolerance = 15
    global score
    if ((abs(x - jack.pos()[0]) <= tolerance)
            and (abs(y - jack.pos()[1]) <= tolerance)):
        score += 1
        pen3.clear()
        pen4.clear()

meadow = turtle.Screen()
meadow.bgcolor("green")
meadow.title("Green Green Grasslands!")
meadow.setup(500,500)
jack = turtle.Turtle("turtle")
jack.penup()
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
pen3 = turtle.Turtle()
pen4 = turtle.Turtle()
pen1.pencolor("yellow")
pen1.hideturtle()
pen1.penup()
pen1.goto(-100, 230)
pen1.pendown()
pen1.write("Score: ", font=("arial", 14, "bold"))
pen2.pencolor("yellow")
pen2.hideturtle()
pen2.penup()
pen2.goto(-100, 210)
pen2.pendown()
pen2.write("Timer: ", font=("arial", 14, "bold"))
pen3.pencolor("yellow")
pen3.hideturtle()
pen3.penup()
pen3.goto(0, 230)
pen4.pencolor("yellow")
pen4.hideturtle()
pen4.penup()
pen4.goto(0, 210)

while timer >= 0:
    pen3.clear()
    pen4.clear()
    pen3.pendown()
    pen4.pendown()
    pen3.write(score, font=("arial", 14, "bold"))
    pen4.write(timer, font=("arial", 14, "bold"))
    jack.goto(random.randint(-200, 200), random.randint(-200, 200))
    time.sleep(1)
    timer -= 1
    meadow.onclick(is_catch)
pen2.clear()
pen4.clear()
pen5 = turtle.Turtle()
pen5.pencolor("black")
pen5.hideturtle()
pen5.penup()
pen5.goto(-120, 200)
pen5.pendown()
pen5.write("G a m e  O v e r!", font=("arial", 20, "bold"))
turtle.done()









