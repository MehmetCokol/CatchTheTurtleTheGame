import turtle
import SetUpScore
import TurtlesInArena



screen = turtle.Screen()
screen.bgcolor("#ccccff")
screen.title("Catch The Turtle The Game")
turtle.tracer(0)

# score turtle
SetUpScore.setupScoreTurtle(screen)
TurtlesInArena.place_turtles(screen)
TurtlesInArena.hide_turtles()
TurtlesInArena.show_turtle_randomly(screen)
SetUpScore.countdown(10,screen)


turtle.tracer(1)
turtle.mainloop()
