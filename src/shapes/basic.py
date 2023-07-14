"""
File         : basic.py
Description  : 
Author       : Alexander Kettler
Creation Date: 14-Jul-2023
"""

import math
import turtle as tur


# ---------------------------------------------------------------------------------------------------------------------

def square(d, rotation: float=90.0):
    tur.right(angle=rotation)
    tur.forward(d)
    tur.right(angle=90)
    tur.forward(d)
    tur.right(angle=90)
    tur.forward(d)
    tur.right(angle=90)
    tur.forward(d)

def hash_square(d):
    size = d
    pos = d / 2
    diag_half = (d * math.sqrt(2)) / 2

    tur.penup()
    tur.goto(-pos, -pos)
    tur.pendown()
    square(size, 270)
    tur.penup()
    tur.goto(0, -diag_half)
    tur.pendown()
    square(size, 45)

    tur.penup()
    tur.home()
    tur.pendown()
