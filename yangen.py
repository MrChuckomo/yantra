"""
File         : yangen.py
Description  : 
Author       : Alexander Kettler
Creation Date: 14-Jul-2023
"""

import typer, toml
import turtle as tur

from PIL import Image
from pathlib import Path
from typing_extensions import Annotated

from src.shapes.basic import hash_square
from src.shapes.medium import inner_circles, leaf, line_dots


# ---------------------------------------------------------------------------------------------------------------------

MAP = {
    'leaf': leaf,
    'line_dots': line_dots,
    'hash_square': hash_square,
    'inner_circles': inner_circles
}

def mapper(data: dict, location: str):
    for shape in data[location]['shape']:
        if 'rep' in shape.keys(): rep_mapper(shape); continue
        for key in shape.keys():
            if type(shape[key]) in [int, float, str, bool]:
                MAP[key](shape[key])
            else:
                print('complex')

def rep_mapper(shape: dict):
    reps = shape['rep']

    for key in shape.keys():
        try:
            func = MAP[key]
            args = shape[key]
        except:
            continue

    for _ in range(0, reps):
        if func and args: func(**args)


def save_image():
    tur.hideturtle()
    canvas = tur.Screen().getcanvas()
    canvas.postscript(file='export/mandala.eps')
    eps_image = Image.open('export/mandala.eps')

    rbga_image = eps_image.convert('RGBA')
    rbga_image.save('export/mandala.png', 'PNG', optimize=True, quality=95)
    rbga_image.close()

    eps_image.close()

# ---------------------------------------------------------------------------------------------------------------------

app = typer.Typer()

@app.command()
def hello(
    input_file: Annotated[Path, typer.Option(help='*.toml file')],
    speed: int=100,
):
    data = toml.loads(input_file.read_text())

    tur.speed(speed)
    tur.hideturtle()
    tur.bgcolor(data['canvas']['bg']['color'])
    tur.color(data['canvas']['pen']['color'])

    mapper(data, 'edges')
    mapper(data, 'inner')

    save_image()


if __name__ == "__main__":
    app()
