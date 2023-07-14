# yantra

<table>
<tbody>
    <tr>
        <td><img src="data/examples/mandala.svg" alt="example"/></td>
        <td><img src="data/examples/mandala2.svg" alt="example"/></td>
        <td><img src="data/examples/mandala3.png" alt="example"/></td>
    </tr>
    <tr>
        <td><img src="data/examples/mandala5.png" alt="example"/></td>
        <td><img src="data/examples/mandala6.png" alt="example"/></td>
        <td><img src="data/examples/mandala7.png" alt="example"/></td>
    </tr>
    <tr>
        <td><img src="data/examples/mandala8.png" alt="example"/></td>
        <td><img src="data/examples/mandala9.png" alt="example"/></td>
        <td><img src="data/examples/mandala10.png" alt="example"/></td>
    </tr>
</tbody>
</table>

# Usage
## Define your Yantra in a `toml` file

```toml
[canvas.bg]
color = 'white'
[canvas.pen]
color = 'black'

[edges]
shape = [
    {hash_square = 600},
    {hash_square = 620}
]

[inner]
shape = [
    {leaf = {size=300, fill=false}, rep=50},
    {leaf = {size=200, fill=false}, rep=50},

    {inner_circles = 90},
    {inner_circles = 60},
    {inner_circles = 25}
]
```

## Run Python CLI

```bash
python yangen.py --input-file y1.toml --speed 100
```

# Development

## Python Environment

```bash
# Manual creation
$ conda env create --prefix ./ops/pyenv/yantra_mandala --file ./environment.yml

# Activate your Python enviroment
$ conda activate yantra_mandala
```

## Dependencies

For macOS: You can install Ghostscript using Homebrew by running the command brew install ghostscript in the Terminal.

For Windows: Download the Ghostscript installer from the official Ghostscript website (https://www.ghostscript.com/download/gsdnld.html), and run the installer to install Ghostscript on your system. Make sure to choose the correct version for your operating system (32-bit or 64-bit).

For Linux: You can install Ghostscript via the package manager for your Linux distribution. For example, on Ubuntu or Debian-based systems, you can use the command sudo apt-get install ghostscript in the terminal.




## Referecnes

- https://realpython.com/beginners-guide-python-turtle/
- [Convert EPS to SVG](https://convertio.co/de/download/185a3a1681360b6814b01239e3ab84037a4e4f/)
- https://pythonturtle.academy/tutorial-drawing-a-flower-petal-or-a-leaf-with-python-turtle/
