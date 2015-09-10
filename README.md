# tortuga

Una aplicación española del módulo turtle.py de Python.

A Spanish implementation of Python's turtle.py module. This removes the langauge-barrier for using Python's Turtle for non-Engish students.

Only the names have been added. The functionality has not changed. This code:

    import tortuga
    t = tortuga.Tortuga()
    t.adelante(100)
    t.izquierda(90)
    t.color_de_lapiz('rojo')
    t.atras(50)

...produces the same output as this:

    import turtle
    t = turtle.Turtle()
    t.forward(100)
    t.left(90)
    t.pencolor('red')
    t.back(50)

The main wiki page for the Turtle Translation project is at https://github.com/asweigart/idle-reimagined/wiki/Turtle-Translations