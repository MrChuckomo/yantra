"""
File         : medium.py
Description  : 
Author       : Alexander Kettler
Creation Date: 14-Jul-2023
"""

import turtle as tur


# ---------------------------------------------------------------------------------------------------------------------

def inner_circles(r: int=25):
    tur.fillcolor('white')
    tur.begin_fill()

    tur.up()
    tur.home()
    tur.forward(r)
    tur.left(90)
    tur.down()
    tur.circle(r)

    tur.end_fill()

    tur.fillcolor('white')
    tur.begin_fill()

    tur.up()
    tur.home()
    tur.forward(r - 5)
    tur.left(90)
    tur.down()
    tur.circle(r - 5)

    tur.end_fill()

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
