import turtle
import random


score = 0
timer = 10
game_over = False

FONT = ("arial", 30, "normal")

screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Green Green Grassland!")
score_pen = turtle.Turtle()
score_pen.hideturtle()
countdown_pen = turtle.Turtle()
countdown_pen.hideturtle()
jack = turtle.Turtle()
jack.hideturtle()
jack.penup()
jack.shape("turtle")
jack.shapesize(2)
max_width = int(screen.window_width() / 2 * 0.75)
max_height = int(screen.window_height() / 2 * 0.75)
jack.speed("fastest")


def setup_score_pen():

    score_pen.color("yellow")
    score_pen.hideturtle()
    score_pen.penup()
    height = screen.window_height() / 2
    score_pen.goto(0, height * 0.9)
    score_pen.clear()
    score_pen.write(f"Score: {score}", align="center", font=FONT)


def countdown(timer):
    global game_over
    countdown_pen.color("yellow")
    countdown_pen.hideturtle()
    countdown_pen.penup()
    height = screen.window_height() / 2
    countdown_pen.goto(0, height * 0.80)

    if timer > 0:
        countdown_pen.clear()
        countdown_pen.write(f"Timer: {timer}", align="center", font=FONT)
        screen.ontimer(lambda: countdown(timer-1),1000)
    else:
        game_over = True
        countdown_pen.clear()
        countdown_pen.write("G a m e  O v e r !", align="center", font=FONT)


def is_catch(x, y):
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"Score: {score}", align="center", font=FONT)


def jumping_jack():
    global game_over
    jack.goto(random.randint(-max_width, max_height),
              random.randint(-max_width, max_height))
    jack.showturtle()
    if not game_over:
        screen.ontimer(jumping_jack,800)
        jack.onclick(is_catch)
    else:
        jack.hideturtle()


def begin():
    global game_over
    game_over = False
    setup_score_pen()
    jumping_jack()
    countdown(timer)


begin()
turtle.mainloop()









