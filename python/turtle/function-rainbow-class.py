#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle as t

def draw_sun():
    t.penup()
    t.goto(-290, 200)

    a = abs(t.pos())

    t.begin_fill()
    t.pendown()
    t.color('red', 'yellow')
    while True:
        t.forward(150)
        t.left(170)

        b = abs(t.pos())

        if (a - 1 < b < a + 1):
            break
    t.penup()
    t.end_fill()

    t.left(90)

def draw_square(color, x=0, y=0, size=70):
    t.penup()
    t.goto(x,y)

    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()

def draw_flower(strong, x, y, size=60):
    draw_square((int(255*strong), int(153*strong), int(153*strong)), x - size, y - size, size)
    draw_square((int(179*strong), int(0*strong), int(179*strong)), x - size, y + size, size)
    draw_square((int(255*strong), int(204*strong), int(255*strong)), x + size, y + size, size)
    draw_square((int(0*strong), int(255*strong), int(255*strong)), x + size, y - size, size)
    draw_square((int(225*strong), int(225*strong), int(128*strong)), x, y, size)

def draw_flower_field():
    for number in range(6):
        draw_flower(0.6, number * 50 + 25, number * 10 - 10, 15)
        draw_flower(0.6, number * -50 - 25, number * 10 - 10, 15)

    for number in range(5):
        draw_flower(0.8, number * 100 + 50, number * 10 - 95, 30)
        draw_flower(0.8, number * -100 - 50, number * 10 - 95, 30)

    for number in range(4):
        draw_flower(1, number * 150 + 75, number * 10 - 230, 45)
        draw_flower(1, number * -150 - 75, number * 10 - 230, 45)

def draw_rainbow_line(color, radius, angle=180, x=0, y=0):
    t.penup()
    t.goto(radius+x, 0+y)
    t.color(color)

    t.pendown()
    t.circle(radius, angle)
    t.penup()

    t.left(360 - angle)

def draw_rainbow():
    center_x = 10
    center_y = 80

    radius = 180
    angle = 120

    # FIXME: Add here a rainbow drawing code

t.setup(width=600, height=600, startx=450, starty=100)
t.speed(0)

t.color('blue')
t.shape("turtle")
t.hideturtle()
t.colormode(255)
t.bgcolor((0, 0, 255))

draw_sun()
draw_flower_field()
draw_rainbow()

t.exitonclick()
