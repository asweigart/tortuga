# This is not a unit test. Instead, it is a general test to make sure the Spanish-named function calls produce an identical drawing.
# This needs to be automated and have more coverage.

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tortuga

tortuga.forward(50)
tortuga.left(90)
tortuga.forward(50)
tortuga.right(45)
tortuga.backward(50)
tortuga.left(45)
tortuga.pensize(5)
for c in ('blue brown orange gray green purple pink yellow white black red'.split()):
    tortuga.color(c)
    tortuga.forward(10)

t = tortuga.Tortuga()
t.subir_lapiz()
t.ir_a(-100, 0)
t.bajar_lapiz()
t.adelante(50)
t.izquierda(90)
t.adelante(50)
t.derecho(45)
t.atras(50)
t.izquierda(45)
t.tamano_lapiz(5)
for c in ('azul marron naranja gris verde morado rosa amarillo blanco negro rojo'.split()):
    t.color(c)
    t.adelante(10)

tortuga.exitonclick()