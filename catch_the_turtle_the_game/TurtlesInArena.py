import turtle
import random
import SetUpScore

score = 0
gridSize = 10
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]
turtles_list = []

def place_turtles(screen):
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y, screen)

def make_turtle(x, y, screen):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        SetUpScore.update_score_turtle(screen, score)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * gridSize, y * gridSize)
    turtles_list.append(t)

def hide_turtles():
    for t in turtles_list:
        t.hideturtle()


#recursive function
def show_turtle_randomly(screen):
    if not SetUpScore.gameOver:
        hide_turtles()
        random.choice(turtles_list).showturtle()
        screen.ontimer(lambda: show_turtle_randomly(screen), 500)
    else:
        hide_turtles()


