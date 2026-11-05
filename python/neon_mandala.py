# =======================================
# ACTIVITY - NEON MANDALA

# PART 1 - IMPORT AND SCREEN SETUP
# turtle.Screen() creates the canvas we draw on.
# bgcolor("black") sets the background -- neon colors pop on black!
# title() stes the next that appears in the windows,s title bar.
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(91)

    board.penup()
    board.goto(0, -60)
    board.setheading(90)
    board.pendown()
    board.color("gold", "yellow")
    board.begin_fill()
    for i in range(5):
        board.forward(130)
        board.right(144)
        board.end_fill()

        board.penup()
        board.goto(0, -60)
        board.setheading(90)
        board.pendown()
        board.color("gold", "yellow")
        board.begin_fill()
        for i in range(5):
            board.forward(130)
            board.right(144)
            board.end_fill()

            board.penup()
            board.goto(0, 0)
            board.pendown()
            petal_colors = ["cyan", "lime", "violet", "orange", "deeppink"]
            for i in range(36):
                board.colors[i % len(petal_colors)],
petal-colors[(i + 2) % len(petal_colors)])
board.begin_fill()
for l in range(4):
    board.forward(55)
    board.right(90)
    board.end_fill()
    board.right(10)

    # KEEP WINDOW OPEN
    turtle.don()



    
