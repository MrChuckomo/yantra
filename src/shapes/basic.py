"""
File         : basic.py
Description  : 
Author       : Alexander Kettler
Creation Date: 14-Jul-2023
"""

import math
import turtle as tur


# ---------------------------------------------------------------------------------------------------------------------

def hexagon(edge_length: int):
    tur.up()
    tur.forward(edge_length)

    tur.right(90)
    tur.down()
    tur.forward(edge_length / 2)
    tur.right(45)
    tur.forward(edge_length)
    tur.right(45)
    tur.forward(edge_length)
    tur.right(45)
    tur.forward(edge_length)
    tur.right(45)
    tur.forward(edge_length)
    tur.right(45)
    tur.forward(edge_length)
    tur.right(45)
    tur.forward(edge_length)
    tur.right(45)
    tur.forward(edge_length)
    tur.right(45)
    tur.forward(edge_length / 2)

    tur.up()
    tur.home()
    tur.down()

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

def diamond(size: int=50):
    tur.right(45)
    tur.forward(size)
    tur.right(90)
    tur.forward(size)

    tur.right(90)
    tur.forward(size)
    tur.right(90)
    tur.forward(size)

    tur.penup()
    tur.home()
    tur.pendown()

def triangle_line(reps: int=10, size: int=50):
    tur.right(45)
    tur.forward(size)
    tur.right(90)
    tur.forward(size)

    for _ in range(0, reps):
        tur.left(90)
        tur.forward(size)
        tur.right(90)
        tur.forward(size)

    tur.penup()
    tur.home()
    tur.pendown()