import sys
import tempfile
import os

try:
    from canvasvg.canvasvg import saveall
except ImportError:
    sys.exit('These tests require the canvasvg module. Run "pip install canvasvg".')


def convert_to_svg_string(canvas):
    canvas.update()
    with tempfile.NamedTemporaryFile(delete=False) as temp_output:
        temp_name = temp_output.name
        saveall(temp_name, canvas)

    # The temp file must be reopened because Windows does not support reading AND writing NamedTemporaryFile.
    with open(temp_name, 'rb') as temp_output:
        content = temp_output.read()
    os.remove(temp_name)

    return content


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
