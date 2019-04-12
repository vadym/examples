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
import random as r

BASE_DISTANCE = 10
BASE_INTERVAL = 7
BASE_ZOOM_INITIAL = 10
BASE_ZOOM_INTENSITY = 0.07
BASE_SIDES = 4

def draw_sun(*colors):
    t.begin_fill()
    t.pendown()
    t.color(*colors)

    a = abs(t.pos())
    while True:
        t.forward(150)
        t.left(170)
        b = abs(t.pos())
        if (a - 1 < b < a + 1):
            break

    t.penup()
    t.end_fill()

def draw_shape(shape_sides = BASE_SIDES, *colors, **kwargs):
    shape_angle = 360 / shape_sides

    zoom = kwargs.get('zoom', BASE_ZOOM_INITIAL)

    t.begin_fill()
    t.pendown()
    t.color(*colors)

    for _ in range(shape_sides):
        t.forward(BASE_DISTANCE * zoom)
        t.left(shape_angle)

    t.fillcolor(colors[0])
    t.penup()
    t.end_fill()

def draw_flower(x, y, **kwargs):
    zoom = kwargs.get('zoom', BASE_ZOOM_INITIAL)

    left = x - BASE_INTERVAL * zoom
    right = x + BASE_INTERVAL * zoom

    top = y + BASE_INTERVAL * zoom
    bottom = y - BASE_INTERVAL * zoom

    t.goto(left, bottom)
    draw_shape(4, 'orange', 'red', zoom=zoom)

    t.goto(left, top)
    draw_shape(4, 'pink', 'red', zoom=zoom)

    t.goto(right, top)
    draw_shape(4, 'purple', 'red', zoom=zoom)

    t.goto(right, bottom)
    draw_shape(4, 'blue', 'red', zoom=zoom)

    t.goto(x, y)
    draw_shape(4, 'yellow', 'red', zoom=zoom)

t.speed(40)
#t.color('blue')
#t.shape("turtle")
t.hideturtle()
t.penup()

t.goto(-200, 200)
draw_sun('red', 'yellow')

draw_flower(0, 0, zoom=5)

t.exitonclick()
