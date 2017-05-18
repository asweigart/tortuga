

Una aplicación española del módulo turtle.py de Python.

A Spanish implementation of Python's turtle.py module. This removes the langauge-barrier for using Python's Turtle for non-Engish students.

Only the names have been added. The functionality has not changed. This code:

    >>> import tortuga
    >>> t = tortuga.Tortuga()
    >>> t.adelante(100)
    >>> t.izquierda(90)
    >>> t.color_de_lapiz('rojo')
    >>> t.atras(50)

...produces the same output as this:

    >>> import turtle
    >>> t = turtle.Turtle()
    >>> t.forward(100)
    >>> t.left(90)
    >>> t.pencolor('red')
    >>> t.back(50)


A full Spanish-language tutorial is being written.

The end goal of the Tortuga project is to add dozens of languages to turtle.py in the Python standard library. A language-switching function (such as `turtle.tortuga()` for Spanish) would change the language used by turtle.py.

# Translation Process

1. The identifiers (i.e. function and method names) and strings (i.e. strings for colors) are translated for a language and added to the Google spreadsheet. Please contact Al at al@inventwithpython.com for access to this spreadsheet.

1. An "identifiers" dictionary is created for the language. For example, for Spanish:

    _SPANISH_IDENTIFIERS = {
    'TurtleScreen': 'PantallaTortuga',
    'RawTurtle': 'TortugaBruta',
    'RawPen':'LapizBruto',
    ...

1. Add the identifiers values to `__all__`

1. A "strings" dictionary is created for the language. For example, for Spanish:

    _SPANISH_STRINGS =
    'negro': 'black',
    'azul': 'blue',
    'marron': 'brown',
    ...

1. TODO - finish this section

# Python Bug / Issue 24990

Adding translations to turtle.py is tracked by this issue on the Python bug tracker:

https://bugs.python.org/issue24990

# TODO

Some of the error messages will also need translations, such as `"stretch_wid/stretch_len must not be zero"`.



The groundwork for translating turtle.py's docstrings has already been laid out. Note the `write_docstringdict()` function's docstring:

    def write_docstringdict(filename="turtle_docstringdict"):
        """Create and write docstring-dictionary to file.

        Optional argument:
        filename -- a string, used as filename
                    default value is turtle_docstringdict

        Has to be called explicitly, (not used by the turtle-graphics classes)
        The docstring dictionary will be written to the Python script <filname>.py
        It is intended to serve as a template for translation of the docstrings
        into different languages.
        """

Note that the `'language'` key in the `_CFG` dictionary and the `_LANGUAGE` variable refer to the language for docstrings, not function or method names. These predate the Tortuga project.