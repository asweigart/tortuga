# tortuga

Una implementación multilingüe del módulo turtle.py de Python. 

A multilingual implementation of Python's turtle.py module.



## Motivation

Turtle graphics has engaged students and beginners to learn programming for a half century. The Python programming language has a `turtle` module that comes with Python. Students write programs that control a "turtle" cursor, drawing lines behind it as it moves around the window. This lets students make generative art programs to create colorful, spirograph-like drawings.

However, all of the functions are in English. There are `forward()` and `left()` functions. But there are not, say, `adelante()` or `izquierda()` function for Spanish-speaking students. 

Tortuga offers the same `turtle` module functions in English but also in the following languages: Spanish, French, German.

(Several other languages are also planned. If you are a native speaker who can volunteer to translate, please contact al@inventwithpython.com)


Only the non-English names have been added. The functionality has not changed. This code:

    >>> from tortuga import *
    >>> adelante(100)
    >>> izquierda(90)
    >>> color_de_lapiz('rojo')
    >>> atras(50)

...produces the same output as this:

    >>> from tortuga import *
    >>> forward(100)
    >>> left(90)
    >>> pencolor('red')
    >>> back(50)

There is no language selection setting in Tortuga. All languages exist in the Tortuga module simultaneously.

For languages that use the Roman alphabet, there are addition ASCII versions that do not use accented letters. For example, Tortuga has both `tamaño_pantalla()` and `tamano_pantalla()` functions.

Tortuga is designed as a single-file Python script. If your computers are unable to install Python packages from PyPI via `pip`, you can always copy the [*__init__.py* file from the GitHub repo](https://github.com/asweigart/tortuga/blob/master/src/tortuga/__init__.py) and rename it as *tortuga.py*.


## What the Tortuga Project is Not

Tortuga is not attempting to translate the Python keywords or the entirety of the Python standard library. Python keywords like `import`, `def`, or `while` will remain in English.

Currently, there are no plans to translate the docstrings for functions or the text of error messages. We can add these if there's a demand for them.

This multi-lingual approach is not a best practice for software design in general, but the specific usage of the `turtle` module as an educational tool for a global audience of non-professional programmers removes a critical barrier to learning to code.



## Documentation and Reference

TODO: This is currently under construction and Tortuga isn't ready for public use. I'm also writing the [Simple Turtle Tutorial](https://github.com/asweigart/simple-turtle-tutorial-for-python/) which is written in a similar style to the [Simple English Wikipedia](https://en.wikipedia.org/wiki/Simple_English_Wikipedia) to facilitate translation into multiple languages. This tutorial's code examples will use Tortuga.

For now, you can examine the `_TRANSLATION_SPREADSHEET` string in the source code to find the names of functions and arguments in all supported languages.


## Special Thanks To

Gregor Lingl for his work on the original turtle.py module.

Ari Lacenski for the Spanish translation
Seunghyo Seo for the Korean translation
Brian Ward and Catherine Devlin for the German translation
Onur Ozay and Erman Korkut for the Turkish translation


## Support

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
