"""
File         : medium.py
Description  : 
Author       : Alexander Kettler
Creation Date: 14-Jul-2023
"""

import turtle as tur


# ---------------------------------------------------------------------------------------------------------------------

def inner_circles(r: int=25, fill: bool=True):
    if fill: tur.fillcolor('white')
    if fill: tur.begin_fill()

    tur.up()
    tur.home()
    tur.forward(r)
    tur.left(90)
    tur.down()
    tur.circle(r)

    if fill: tur.end_fill()

    if fill: tur.fillcolor('white')
    if fill: tur.begin_fill()

    tur.up()
    tur.home()
    tur.forward(r - 5)
    tur.left(90)
    tur.down()
    tur.circle(r - 5)

    if fill: tur.end_fill()

    tur.penup()
    tur.home()
    tur.pendown()


def leaf(size: int=300, fill: bool=False):
    if fill: tur.fillcolor('white')
    if fill: tur.begin_fill()
    tur.circle(size, 70)
    tur.left(110)
    tur.circle(size, 70)
    if fill: tur.end_fill()

    # tur.penup()
    # tur.home()
    # tur.pendown()


def line_dots(length: int=100, angle: int=90, circle_r: int=10):
    tur.up()
    tur.home()
    tur.down()

    tur.left(angle)
    tur.forward(length)
    tur.circle(circle_r)
    tur.right(90)
    tur.circle(circle_r)
    tur.right(90)
    tur.circle(circle_r)
