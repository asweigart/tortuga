# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='Tortuga',
    version='0.0.7',
    url='https://github.com/asweigart/tortuga',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=("Una implementación multilingüe del módulo Turtle.py de Python. A multilingual implementation of Python's turtle.py module."),
    license='BSD',
    packages=['tortuga'],
    install_requires=[''],
    test_suite='tests',
    keywords="turtle logo spanish multilingual i18n",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)