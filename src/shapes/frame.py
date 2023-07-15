"""
File         : frame.py
Description  : 
Author       : Alexander Kettler
Creation Date: 14-Jul-2023
"""

import math
import turtle as tur

from src.shapes.basic import square, triangle_line


# ---------------------------------------------------------------------------------------------------------------------

def plus_frame(layer: int=2):
    def plus_side(layer: int=1, start_angle: int=0):
        offset = 5 * layer
        tur.right(start_angle)
        tur.up()
        tur.forward(350 - offset)
        tur.down()
        tur.right(90)
        tur.forward(90 - offset)
        tur.right(90)
        tur.forward(70 - offset)
        tur.right(90)
        tur.forward(60 - offset)
        tur.left(90)
        tur.forward(50 + offset)     #! neck
        tur.left(90)
        tur.forward(200 - offset)

        tur.up()
        tur.home()
        tur.right(start_angle)

        tur.up()
        tur.forward(350 - offset)
        tur.down()
        tur.left(90)
        tur.forward(90 - offset)
        tur.left(90)
        tur.forward(70 - offset)
        tur.left(90)
        tur.forward(60 - offset)
        tur.right(90)
        tur.forward(50 + offset)     #! neck
        tur.right(90)
        tur.forward(200 - offset)

        tur.up()
        tur.home()
        tur.pendown()

    for l in range(0, layer):
        plus_side(layer=l, start_angle=0)
        plus_side(layer=l, start_angle=90)
        plus_side(layer=l, start_angle=180)
        plus_side(layer=l, start_angle=270)


def corner_frame(layer: int=2):
    def corner_stone(layer: int=1, start_angle: int=0):
        offset = 7 * layer
        tur.right(start_angle)

        tur.up()
        tur.forward(300 - offset)
        tur.down()
        tur.right(90)
        tur.forward(250 - offset)

        #! Corner
        tur.left(90)
        tur.forward(50 - offset)
        tur.right(90)
        tur.forward(100 - offset)
        tur.right(90)
        tur.forward(100 - offset)
        tur.right(90)
        tur.forward(50 - offset)

        tur.left(90)
        tur.forward(250 - offset)

        tur.up()
        tur.home()
        tur.pendown()

    for l in range(0, layer):
        corner_stone(layer=l, start_angle=0)
        corner_stone(layer=l, start_angle=90)
        corner_stone(layer=l, start_angle=180)
        corner_stone(layer=l, start_angle=270)

def triangle_frame(fill: bool=False):
    tur.goto(315, 315)
    tur.home()
    tur.goto(315, -315)
    tur.home()
    tur.goto(-315, -315)
    tur.home()
    tur.goto(-315, 315)
    tur.home()

    tur.up()
    tur.goto(300, 300)
    tur.down()

    if fill: tur.fillcolor('white')
    if fill: tur.begin_fill()
    square(600)
    if fill: tur.end_fill()

    #! right
    triangle_line(20, 20)

    #! top
    tur.up()
    tur.goto(-300, 300)
    tur.down()
    tur.left(90)

    triangle_line(20, 20)

    #! bottom
    tur.up()
    tur.goto(300, -300)
    tur.down()
    tur.right(90)

    triangle_line(20, 20)

    #! left
    tur.up()
    tur.goto(-300, -300)
    tur.down()
    tur.left(180)

    triangle_line(20, 20)

    tur.up()
    tur.goto(315, 315)
    tur.down()
    square(630)

def circle_edge(radius: int=100, points: int=50, shape_dim: int=10):
    tur.goto(0, 0)

    for i in range(points + 1):
        # theta = i * (math.pi / (2 * points))  # 1/4 circle
        theta = i * (2 * math.pi / points)  # full circle

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        tur.up()
        tur.goto(x, y)
        tur.down()

        tur.circle(shape_dim)

    tur.up()
    tur.home()
    tur.down()
