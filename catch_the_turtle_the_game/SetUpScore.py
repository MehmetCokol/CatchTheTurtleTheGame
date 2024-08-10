import turtle


FONT = ["Arial", 30, "normal"]
scoreTurtle = None
countdownTurtle = None
gameOver = False


def setupScoreTurtle(screen):
    global scoreTurtle
    scoreTurtle = turtle.Turtle()
    scoreTurtle.hideturtle()
    scoreTurtle.color("blue")
    scoreTurtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.88
    scoreTurtle.setpos(0, y)
    scoreTurtle.clear()
    scoreTurtle.write("Score: 0", False, "center", FONT)


def update_score_turtle(screen, score):
    global scoreTurtle
    scoreTurtle.clear()
    scoreTurtle.write("Score: {}".format(score), False, "center", FONT)


def countdown(time, screen):
    global countdownTurtle
    global gameOver

    if countdownTurtle is None:
        countdownTurtle = turtle.Turtle()
        countdownTurtle.hideturtle()
        countdownTurtle.color("black")
        countdownTurtle.penup()
        top_height = screen.window_height() / 2
        y = top_height * 0.88
        countdownTurtle.setpos(0, y - 40)

    countdownTurtle.clear()

    if time > 0:
        countdownTurtle.write("Time: {}".format(time), False, "center", FONT)
        screen.ontimer(lambda: countdown(time - 1, screen), 1000)
    else:

        countdownTurtle.clear()
        countdownTurtle.color("Red")

        countdownTurtle.write("GAME OVER!", False, "center", FONT)
        gameOver=True
