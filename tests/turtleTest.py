import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import turtle
import unittest
from unittest import TestCase
import tortuga
import testUtil

spanish_colors = 'azul marron naranja gris verde morado rosa amarillo blanco negro rojo'.split()
english_colors = 'blue brown orange gray green purple pink yellow white black red'.split()


class TestBasicModuleFunctionality(TestCase):
    def setUp(self):
        self.clear()

    def clear(self):
        turtle.clear()
        tortuga.clear()

    def assert_same(self):
        testUtil.assert_canvas_equal(turtle.getscreen().getcanvas(), tortuga.getscreen().getcanvas())

    def assert_different(self):
        testUtil.assert_canvas_not_equal(turtle.getscreen().getcanvas(), tortuga.getscreen().getcanvas())

    def test_simple_functions(self):
        turtle.forward(50)
        turtle.left(90)

        tortuga.forward(50)
        tortuga.left(90)
        self.assert_same()

    def test_pencolor(self):
        for c in (spanish_colors):
            tortuga.color_de_lapiz(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.pencolor(c)
            turtle.forward(3)

        self.assert_same()

    def test_fillcolor(self):
        for c in (spanish_colors):
            tortuga.color_de_relleno(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.fillcolor(c)
            turtle.forward(3)

        self.assert_same()

    def test_color(self):
        for c in (spanish_colors):
            tortuga.color(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.color(c)
            turtle.forward(3)

        self.assert_same()

    def test_bgcolor(self):
        for c in (spanish_colors):
            tortuga.color_fondo(c)
            tortuga.forward(3)

        for c in (english_colors):
            turtle.bgcolor(c)
            turtle.forward(3)

        self.assert_same()

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
        self.assert_same()

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
        self.assert_same()

    def test_pen(self):
        some_english_colors = ['blue', (0.5, 0.3, 0.2), 'brown', 'orange']
        some_spanish_colors = ['azul', (0.5, 0.3, 0.2), 'marron', 'naranja']
        pen_options = [('shown', 'se_muestra', [True, False]),
                       ('pendown', 'bajar_lapiz', [True, False]),
                       ('pencolor', 'color_de_lapiz', some_english_colors, some_spanish_colors),
                       ('fillcolor', 'color_de_relleno', some_english_colors, some_spanish_colors),
                       ('pensize', 'tamano_lapiz', [1, 2, 3, 4, 5]),
                       ('speed', 'velocidad', range(1, 11)),
                       ('resizemode', 'modo_cambio_tamano', ['auto', 'user', 'noresize'], ['auto', 'usuario', 'sin cambio de tamano']),
                       ('stretchfactor', 'TODO: stretchfactor', [(1, 1), (1, 2), (2, 1), (2, 2)]),
                       ('outline', 'TODO: outline', [1, 2, 3]),
                       ('tilt', 'rotar', [1, 2, 3])]

        for entry in pen_options:
            english_key = entry[0]
            spanish_key = entry[1]
            english_values = entry[2]
            if len(entry) > 3:
                spanish_values = entry[3]
            else:
                spanish_values = english_values

            for english_value, spanish_value in zip(english_values, spanish_values):
                self.clear()
                tortuga.pen(**{english_key: english_value})
                tortuga.forward(3)

                turtle.pen(**{english_key: english_value})
                turtle.forward(3)

                tortuga.pen(**{english_key: spanish_value})
                tortuga.forward(3)

                turtle.pen(**{english_key: english_value})
                turtle.forward(3)

                tortuga.pen(**{spanish_key: spanish_value})
                tortuga.forward(3)

                turtle.pen(**{english_key: english_value})
                turtle.forward(3)
                self.assert_same()

    def test_shape(self):
        english_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
        spanish_shapes = ['flecha', 'tortuga', 'circulo', 'cuadrado', 'triangulo', 'clasico']

        for english_shape, spanish_shape in zip(english_shapes, spanish_shapes):
            tortuga.shape(spanish_shape)
            tortuga.forward(3)
            tortuga.figura(spanish_shape)
            tortuga.forward(3)
            tortuga.shape(english_shape)
            tortuga.forward(3)

            turtle.shape(english_shape)
            turtle.forward(3)
            turtle.shape(english_shape)
            turtle.forward(3)
            turtle.shape(english_shape)
            turtle.forward(3)

    def test_resizemode(self):
        english_options = ['auto', 'user', 'noresize']
        spanish_options = ['auto', 'usuario', 'sin_cambio_de_tamano']

        for english_option, spanish_option in zip(english_options, spanish_options):
            tortuga.resizemode(spanish_option)
            tortuga.forward(3)
            tortuga.modo_cambio_tamano(spanish_option)
            tortuga.forward(3)
            tortuga.resizemode(english_option)
            tortuga.forward(3)

            turtle.resizemode(english_option)
            turtle.forward(3)
            turtle.resizemode(english_option)
            turtle.forward(3)
            turtle.resizemode(english_option)
            turtle.forward(3)


class TestBasicMethodFunctionality(TestCase):
    def setUp(self):
        self.clear()

    def clear(self):
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

    def test_pen(self):
        some_english_colors = ['blue', (0.5, 0.3, 0.2), 'brown', 'orange']
        some_spanish_colors = ['azul', (0.5, 0.3, 0.2), 'marron', 'naranja']
        pen_options = [('shown', 'se_muestra', [True, False]),
                       ('pendown', 'bajar_lapiz', [True, False]),
                       ('pencolor', 'color_de_lapiz', some_english_colors, some_spanish_colors),
                       ('fillcolor', 'color_de_relleno', some_english_colors, some_spanish_colors),
                       ('pensize', 'tamano_lapiz', [1, 2, 3, 4, 5]),
                       ('speed', 'velocidad', range(1, 11)),
                       ('resizemode', 'modo_cambio_tamano', ['auto', 'user', 'noresize'], ['auto', 'usuario', 'sin_cambio_de_tamano']),
                       ('stretchfactor', 'TODO: stretchfactor', [(1, 1), (1, 2), (2, 1), (2, 2)]),
                       ('outline', 'TODO: outline', [1, 2, 3]),
                       ('tilt', 'rotar', [1, 2, 3])]

        for entry in pen_options:
            english_key = entry[0]
            spanish_key = entry[1]
            english_values = entry[2]
            if len(entry) > 3:
                spanish_values = entry[3]
            else:
                spanish_values = english_values

            for english_value, spanish_value in zip(english_values, spanish_values):
                self.clear()
                self.tortuga.pen(**{english_key: english_value})
                self.tortuga.forward(3)

                self.turtle.pen(**{english_key: english_value})
                self.turtle.forward(3)

                self.tortuga.pen(**{english_key: spanish_value})
                self.tortuga.forward(3)

                self.turtle.pen(**{english_key: english_value})
                self.turtle.forward(3)

                self.tortuga.pen(**{spanish_key: spanish_value})
                self.tortuga.forward(3)

                self.turtle.pen(**{english_key: english_value})
                self.turtle.forward(3)
                self.assert_same()

    def test_shape(self):
        english_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
        spanish_shapes = ['flecha', 'tortuga', 'circulo', 'cuadrado', 'triangulo', 'clasico']

        for english_shape, spanish_shape in zip(english_shapes, spanish_shapes):
            self.tortuga.shape(spanish_shape)
            self.tortuga.forward(3)
            self.tortuga.figura(spanish_shape)
            self.tortuga.forward(3)
            self.tortuga.shape(english_shape)
            self.tortuga.forward(3)

            self.turtle.shape(english_shape)
            self.turtle.forward(3)
            self.turtle.shape(english_shape)
            self.turtle.forward(3)
            self.turtle.shape(english_shape)
            self.turtle.forward(3)

    def test_resizemode(self):
        english_options = ['auto', 'user', 'noresize']
        spanish_options = ['auto', 'usuario', 'sin_cambio_de_tamano']

        for english_option, spanish_option in zip(english_options, spanish_options):
            self.tortuga.resizemode(spanish_option)
            self.tortuga.forward(3)
            self.tortuga.modo_cambio_tamano(spanish_option)
            self.tortuga.forward(3)
            self.tortuga.resizemode(english_option)
            self.tortuga.forward(3)

            self.turtle.resizemode(english_option)
            self.turtle.forward(3)
            self.turtle.resizemode(english_option)
            self.turtle.forward(3)
            self.turtle.resizemode(english_option)
            self.turtle.forward(3)

if __name__ == '__main__':
    unittest.main()
