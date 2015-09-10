import turtle
from unittest import TestCase
import tortuga
import testUtil

spanish_colors = 'azul marron naranja gris verde morado rosa amarillo blanco negro rojo'.split()
english_colors = 'blue brown orange gray green purple pink yellow white black red'.split()


class TestBasicModuleFunctionality(TestCase):
    def setUp(self):
        turtle.clear()
        tortuga.clear()

    def assert_module_same(self):
        testUtil.assert_canvas_equal(turtle.getscreen().getcanvas(), tortuga.getscreen().getcanvas())

    def assert_module_different(self):
        testUtil.assert_canvas_not_equal(turtle.getscreen().getcanvas(), tortuga.getscreen().getcanvas())

    def test_simple_functions(self):
        turtle.forward(50)
        turtle.left(90)

        tortuga.forward(50)
        tortuga.left(90)
        self.assert_module_same()

    def test_pencolor(self):
        for c in (spanish_colors):
            tortuga.color_de_lapiz(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.pencolor(c)
            turtle.forward(3)

        self.assert_module_same()

    def test_fillcolor(self):
        for c in (spanish_colors):
            tortuga.color_de_relleno(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.fillcolor(c)
            turtle.forward(3)

        self.assert_module_same()

    def test_color(self):
        for c in (spanish_colors):
            tortuga.color(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.color(c)
            turtle.forward(3)

        self.assert_module_same()

    def test_bgcolor(self):
        for c in (spanish_colors):
            tortuga.color_fondo(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.bgcolor(c)
            turtle.forward(3)

        self.assert_module_same()

    def test_same_function_names_work(self):
        # draw some things using the english commands in tortuga
        tortuga.forward(50)
        tortuga.left(90)
        tortuga.forward(50)
        tortuga.right(45)
        tortuga.backward(50)
        tortuga.left(45)
        tortuga.pensize(5)
        for c in (english_colors):
            tortuga.color(c)
            tortuga.forward(10)

        # now draw the same things using turtle
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(45)
        turtle.backward(50)
        turtle.left(45)
        turtle.pensize(5)
        for c in (english_colors):
            turtle.color(c)
            turtle.forward(10)

        # and make sure they both resulted in the same output
        self.assert_module_same()

    def test_equivalent_spanish_names_work(self):
        # draw some things using the english commands in tortuga
        tortuga.adelante(50)
        tortuga.izquierda(90)
        tortuga.adelante(50)
        tortuga.derecho(45)
        tortuga.atras(50)
        tortuga.izquierda(45)
        tortuga.tamano_lapiz(5)
        for c in (english_colors):
            tortuga.color(c)
            tortuga.adelante(10)
        for c in (spanish_colors):
            tortuga.color(c)
            tortuga.adelante(10)

        # now draw the same things using turtle
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(45)
        turtle.backward(50)
        turtle.left(45)
        turtle.pensize(5)
        for c in (english_colors):
            turtle.color(c)
            turtle.forward(10)
        for c in (english_colors):
            turtle.color(c)
            turtle.forward(10)

        # and make sure they both resulted in the same output
        self.assert_module_same()


class TestBasicMethodFunctionality(TestCase):
    def setUp(self):
        self.turtle = turtle.Turtle()
        self.tortuga = tortuga.Tortuga()

    def assert_same(self):
        testUtil.assert_canvas_equal(self.turtle.getscreen().getcanvas(), self.tortuga.getscreen().getcanvas())

    def assert_different(self):
        testUtil.assert_canvas_not_equal(self.turtle.getscreen().getcanvas(), self.tortuga.getscreen().getcanvas())

    def test_simple_methods(self):
        self.turtle.forward(50)
        self.turtle.left(90)

        self.tortuga.forward(50)
        self.tortuga.left(90)
        self.assert_same()

    def test_same_method_names_work(self):
        # draw some things using the english commands in tortuga
        self.tortuga.forward(50)
        self.tortuga.left(90)
        self.tortuga.forward(50)
        self.tortuga.right(45)
        self.tortuga.backward(50)
        self.tortuga.left(45)
        self.tortuga.pensize(5)
        for c in (english_colors):
            self.tortuga.color(c)
            self.tortuga.forward(10)

        # now draw the same things using turtle
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(45)
        self.turtle.backward(50)
        self.turtle.left(45)
        self.turtle.pensize(5)
        for c in (english_colors):
            self.turtle.color(c)
            self.turtle.forward(10)

        # and make sure they both resulted in the same output
        self.assert_same()

    def test_equivalent_spanish_names_work(self):
        # draw some things using the english commands in tortuga
        self.tortuga.adelante(50)
        self.tortuga.izquierda(90)
        self.tortuga.adelante(50)
        self.tortuga.derecho(45)
        self.tortuga.atras(50)
        self.tortuga.izquierda(45)
        self.tortuga.tamano_lapiz(5)
        for c in (english_colors):
            self.tortuga.color(c)
            self.tortuga.adelante(10)
        for c in (spanish_colors):
            self.tortuga.color(c)
            self.tortuga.adelante(10)

        # now draw the same things using turtle
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(45)
        self.turtle.backward(50)
        self.turtle.left(45)
        self.turtle.pensize(5)
        for c in (english_colors):
            self.turtle.color(c)
            self.turtle.forward(10)
        for c in (english_colors):
            self.turtle.color(c)
            self.turtle.forward(10)

        # and make sure they both resulted in the same output
        self.assert_same()

    def test_pencolor(self):
        for c in (spanish_colors):
            self.tortuga.color_de_lapiz(c)
            self.tortuga.forward(3)

        for c in (english_colors):
            self.turtle.pencolor(c)
            self.turtle.forward(3)

        self.assert_same()

    def test_fillcolor(self):
        for c in (spanish_colors):
            self.tortuga.color_de_relleno(c)
            self.tortuga.forward(3)

        for c in (english_colors):
            self.turtle.fillcolor(c)
            self.turtle.forward(3)

        self.assert_same()

    def test_color(self):
        for c in (spanish_colors):
            self.tortuga.color(c)
            self.tortuga.forward(3)

        for c in (english_colors):
            self.turtle.color(c)
            self.turtle.forward(3)

        self.assert_same()
