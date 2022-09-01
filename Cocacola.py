#cocacola ASCII art


from turtle import Screen, Turtle

PIXEL_SIZE = 10
CURSOR_SIZE = 20

COLORS = {
    'R': 'red',
    'W': 'white',
}

PIXELS = [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "RRRRRRRRRRRRRRRWWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWRRRRWWWWWWWRRRRRRRRRRWWWRRRRRR",
    "RRRRRRRRRRRRRWWWWWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWWWWWWWWWWWWWRRRRRRWWWWWRRRRWR",
    "RRRRRRRRRRRWWWWWRRWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWRRWWRRRWWWWWWWWRRRRWWWRRWRRWWRR",
    "RRRRRRRRRRWWWWWRRWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWRRWRRRRRRRWWWWWWWRRWWWRRRRRWWWRR",
    "RRRRRRRRRWWWWWRRRWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWRRRRRWRRRRRRRWWWWWRWWWRRRWWWWWRRR",
    "RRRRRRRRWWWWWRRRRWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWRRWRRRWRRRRRRRRWWWRWWWRRWWWWWWRRRR",
    "RRRRRRRWWWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWRRWWRRRRRRRRRRRRRRRWWWWRWWWWWWRRRRR",
    "RRRRRRWWWWWRRRRRWWWWRRRRRRRWWWRRRRRRWWWWWWWRRWWWRRWWWWWRRRWRRRWRRRRRRRRRRRRWWWRWWWWWRRRRRRR",
    "RRRRRWWWWWWRRRRWWWWWRRRRRRWWWWWRRRRWWWWWWWWRWWWWRWWWWWRRRWWRRRRRRRRRRRRRRRWWWRRWRRRRRRRRRRR",
    "RRRRRWWWWWRRRRWWWRRWWRRRWWWWRWWRRRWWWRWWWWRWWWWRRWWWWRRRRWWRRWRRRRRRRRRRRWWWWRRRWRRRRRRRRRR",
    "RRRRWWWWWRRRRWWWWRRWWRRRWWWRWWWRRWWWRRWWWWRWWWRRWWWWWRRRRWWRWRRRRRRRRRRRRWWWRRRWWRRRRRRRRRR",
    "RRRRWWWWWRRRWWWWWRRWRRRWWWRRWWRRWWWWRRWWWRRRRRRWWWWWRRRRRRWWRRRRRRRRRRRRWWWWRRWWRRRRRRRRRRR",
    "RRRWWWWWRRRRWWWWWWWWWWWWWWRRWRRWWWWRRWWWWRRRRRRWWWWWRRRRRRRRRRRRRRRRRRRRWWWRRRWRRRRRRRRRRRR",
    "RRRWWWWWRRRWWWWRRWWWWWWWWRRRRRRWWWRRRWWWRRRRRRWWWWWRRRRRRRRRRRRRRRRRRRRWWWWRRWRRRRRRRRRRRRR",
    "RRWWWWWRRRRWWWRRRRWRRWWWWRRRRRWWWWRRWWWWRWRRRRWWWWRRRRWWWRRRRRRRWWRRRRWWWWRRWWRRWWWRWWWRRRR",
    "RRWWWWWRRRWWWWRRRWWRWWWWRRRRRWWWWRRRWWWRRWRRRWWWWWRRRWWWWWRRRRRWWWWRRRWWWWRWWRRWWWWWWWWRRRR",
    "RWWWWWRRRRWWWWRRWWRRWWWWRRRRWWWWWRRWWWWRWRRRRWWWWWRRWWWRRWRRRRWWRRWRRRWWWRWWRRWWWRRWWWRRRRR",
    "RWWWWWRRRRWWWRRWWRRRWWWWRRRRWWWWWRWWWWRWWRRRWWWWWRRWWWWRRWRRRWWWRRWRRWWWWWWRRWWWRRWWWWRRRRR",
    "RWWWWWRRRWWWWWWWWRRRWWWWRRWWWWWWWWWWWWWWRRRRWWWWWRRWWWRRRWRRRWWWRRWRRWWWWWRRWWWWRRWWWRRRRRR",
    "RWWWWWRRRRWWWWWWRRRRWWWWWWWRRWWWWWWWWWWRRRRRWWWWRRWWWWRRRWRRWWWWWWWRWWWWRRRRWWWRRWWWWRRRRRR",
    "RWWWWRRRRRWWWWWRRRRRWWWWWWRRRWWWWRWWWWRRRRRWWWWWRRWWWWRRWWRWWWRRWWWWWWWWRRRWWWRRRWWWRRRRRRR",
    "RWWWWRRRRRRWWRRRRRRRRWWWRRRRRWWWRRWWWRRRRRRWWWWWRRWWWRRRWRRWWRRRWWRWWWWRRRWWWWRRWWWWRWRRRRR",
    "RWWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWRWWRRRRWWRWWWRRRWRRWWWWRRRWWWWRRWWWRRWRRRRR",
    "RWWWWWRRRRRRRRRRRRRRRRRRRRWWWWWRRRRRRRRRRRRWWWWWRRRRRRWWRRWWRRRRWRRWWWWRRWWWWRRWWWWRWRRRRRR",
    "RWWWWWRRRRRRRRRRRRRRRWWWWWWWWWWWWWWRRRRRRRRWWWWWRRRRRRWRRRWWRRRWRRRWWWWRWWWWWRWWWWRWWRRRRRR",
    "RRWWWWWRRRRRRRRRRRWWWWWWWWWWWWWWWWWWWRRRRRRRWWWWRRRRWWWRRRWWWWWRRRRWWWWWWWWWWWWWWWWWRWWWWRR",
    "RRRWWWWWRRRRRRWWWWWWRRRRRRRWWWWWWWWWWWWRRRRRWWWWWWRWWWRRRRWWWWWRRRRWWWWWWWWWWWWWWWWRRRWWWRR",
    "RRRRWWWWWWWWWWWWRRRRRRRRRRRRRWWWWWWWWWWWRRRRRWWWWWWWRRRRRRWWWWRRRRRWWWWWRWWWWRWWWWRRRRWWWRR",
    "RRRRRRWWWWWWRRRRRRRRRRRRRRRRRRWRRRRRRRWWWRRRRRWWWWRRRRRRRRRWRRRRRRRRWWRRRRWWRRRWRRRRRWWWWRR",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
]


WIDTH, HEIGHT = len(PIXELS[0]), len(PIXELS)

screen = Screen()
screen.setup((WIDTH + 3) * PIXEL_SIZE, (HEIGHT + 3) * PIXEL_SIZE)
screen.tracer(False)

turtle = Turtle()
turtle.hideturtle()
turtle.shape('square')
turtle.shapesize(PIXEL_SIZE / CURSOR_SIZE)
turtle.penup()

x0 = -WIDTH/2 * PIXEL_SIZE
y0 = HEIGHT/2 * PIXEL_SIZE

for i, row in enumerate(PIXELS):
    turtle.setposition(x0, y0 - i * PIXEL_SIZE)

    for pixel in row:
        turtle.color(COLORS[pixel])
        turtle.stamp()
        turtle.forward(PIXEL_SIZE)

screen.tracer(True)
screen.exitonclick()
