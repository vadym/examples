import turtle as t


def draw_shape(sides, length):
    t.begin_fill()

    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)
        t.end_fill()


def draw_matrix(matrix):
    t.color('yellow')
    t.speed(100)

    startX = -200
    startY = 200

    shapeSide = 50

    for col in range(len(matrix[row])):
        for row in range(len(matrix)):
            cell = matrix[row][col]

            if cell == 1:
                t.color("black")
            elif cell == 2:
                t.color("red")
            elif cell == 3:
                t.color("blue")
            else:
                t.color("yellow")

            curX = startX + shapeSide * col + col * 2
            curY = startY - shapeSide * row - row * 2

            t.penup()
            t.goto(curX, curY)
            t.pendown()

            draw_shape(4, shapeSide)

matrixSmile = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 3, 3, 1, 1, 3, 3, 1],
        [0, 3, 3, 0, 0, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 2, 0, 0, 0]
    ]

t.setup(width=600, height=600, startx=0, starty=0)
t.hideturtle()

draw_matrix(matrixSmile)

t.exitonclick()
