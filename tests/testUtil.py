# add canvasvg to requirements for running these tests

from canvasvg.canvasvg import saveall
import tempfile


def convert_to_svg_string(canvas):
    canvas.update()
    with tempfile.NamedTemporaryFile() as temp_output:
        saveall(temp_output.name, canvas)
        return open(temp_output.name, "rb").read()


def to_svgs(canvas1, canvas2):
    svg1 = convert_to_svg_string(canvas1)
    svg2 = convert_to_svg_string(canvas2)
    return svg1, svg2


def assert_canvas_equal(canvas1, canvas2):
    svg1, svg2 = to_svgs(canvas1, canvas2)
    assert svg1 == svg2


def assert_canvas_not_equal(canvas1, canvas2):
    svg1, svg2 = to_svgs(canvas1, canvas2)
    assert svg1 != svg2
