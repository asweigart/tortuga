

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

# What the Tortuga Project is Not

Tortuga is not attempting to translate the Python keywords or the entirety of the Python standard library. T

# Things to Translate

- Module names (so that `import turtle` can be replaced by `from turtle import tortuga`)
- Function, method, and class names
- Strings that are passed to and returned from these functions & methods.
- The docstrings and `help()` system
- The Python documentation for turtle.py
- Error messages from turtle.py
- An example-based turtle tutorial written in "simple English"

# Instructions for Translators

1. Go to the Google spreadsheet (ask Al for the URL: al@inventwithpython.com or @AlSweigart on Twitter)

1. Open up https://scratch.mit.edu and click Create at the top to run the Scratch editor. For general consistency, we'll be copying the translations from Scratch where we can. The "In Scratch UI" column will tell you which Scratch category (the colored labels at the top-middle part of the page, e.g. Motion, Looks, Pen). You can see the translations by clicking the globe icon in the menu bar and selecting a language.

1. Fill in the translatons. Use the correct PEP-8 naming schemes: CapitalizedLetters for class names, lowercase_separated_by_underscores for everything else. Note that many of the English function names don't use underscores (such as `pencolor` or `showturtle`, but this is a mistake. Use underscores in your translatons.

1. Translated names can include accented characters and unicode, but can't include apostraphes. Use a name that makes the most sense in the translated language.

1. Double check for spelling and formatting. These translations need to be perfect since they can't easily be changed later on.

# Process for Adding Translations to Code

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

1. Translate the simple English tutorial


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

TODO - change help() text

# Additional Work

It'd be great to add this to the http://pythonturtle.org website, which provides stand-alone installers for using turtle.py. This project hasn't been maintained in a while and I'm not sure about its current popularity, but it could make use of the internationalization work of Tortuga.

It's GitHub page is https://github.com/cool-RR/PythonTurtle

# Special Thanks To

Gregor Lingl for his work on the original turtle.py module.

Ari Lacenski for the Spanish translation
Seunghyo Seo for the Korean translation
Brian Ward and Catherine Devlin for the German translation
Onur Ozay and Erman Korkut for the Turkish translation


Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
