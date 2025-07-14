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

There is no language selection setting in Tortuga. Function names in all languages exist in the Tortuga module simultaneously.

For languages that use the Roman alphabet, there are addition ASCII versions that do not use accented letters. For example, Tortuga has both `tamaño_pantalla()` and `tamano_pantalla()` functions.

Tortuga is designed as a single-file Python script. If your computers are unable to install Python packages from PyPI via `pip`, you can always copy the [*\_\_init\_\_.py* file from the GitHub repo](https://github.com/asweigart/tortuga/blob/master/src/tortuga/__init__.py) and rename it as *tortuga.py*.


## What the Tortuga Project is Not

Tortuga is not attempting to translate the Python keywords or the entirety of the Python standard library. Python keywords like `import`, `def`, or `while` will remain in English.

Currently, there are no plans to translate the docstrings for functions or the text of error messages. We can add these if there's a demand for them.

This multi-lingual approach is not a best practice for software design in general, but the specific usage of the `turtle` module as an educational tool for a global audience of non-professional programmers removes a critical barrier to learning to code.



## Documentation and Reference

The following table contains the equivalent functions and arguments for Tortuga.

### Español/Spanish

| English | Spanish | Spanish ASCII |
| --- | --- | --- |
| `bgcolor()` | `color_fondo()` | `color_fondo()` |
| `bgpic()` | `imagen_fondo()` | `imagen_fondo()` |
| `bye()` | `adiós()` | `adios()` |
| `clearscreen()` | `borrar_pantalla()` | `borrar_pantalla()` |
| `colormode()` | `modo_color()` | `modo_color()` |
| `delay()` | `retraso()` | `retraso()` |
| `done()` | `hecho()` | `hecho()` |
| `exitonclick()` | `salir_al_hacer_clic()` | `salir_al_hacer_clic()` |
| `getcanvas()` | `obtener_lienzo()` | `obtener_lienzo()` |
| `getshapes()` | `obtener_formas()` | `obtener_formas()` |
| `listen()` | `enfocar_ventana()` | `enfocar_ventana()` |
| `mainloop()` | `bucle_principal()` | `bucle_principal()` |
| `mode()` | `modo()` | `modo()` |
| `no_animation()` | `sin_animación()` | `sin_animacion()` |
| `numinput()` | `ingresar_número()` | `ingresar_numero()` |
| `onkey()` | `al_presionar_tecla()` | `al_presionar_tecla()` |
| `onkeypress()` | `al_pulsar_tecla()` | `al_pulsar_tecla()` |
| `onkeyrelease()` | `al_soltar_tecla()` | `al_soltar_tecla()` |
| `onscreenclick()` | `al_hacer_clic_en_pantalla()` | `al_hacer_clic_en_pantalla()` |
| `ontimer()` | `en_temporizador()` | `en_temporizador()` |
| `register_shape()` | `agregar_forma()` | `agregar_forma()` |
| `resetscreen()` | `reiniciar_pantalla()` | `reiniciar_pantalla()` |
| `save()` | `ahorrar()` | `ahorrar()` |
| `screensize()` | `tamaño_pantalla()` | `tamano_pantalla()` |
| `setup()` | `configurar()` | `configurar()` |
| `setworldcoordinates()` | `establecer_coordenadas_mundo()` | `establecer_coordenadas_mundo()` |
| `textinput()` | `ingresar_texto()` | `ingresar_texto()` |
| `title()` | `título()` | `titulo()` |
| `tracer()` | `tasa_dibujo()` | `tasa_dibujo()` |
| `turtles()` | `tortugas()` | `tortugas()` |
| `update()` | `actualizar()` | `actualizar()` |
| `window_height()` | `altura_la_ventana()` | `altura_la_ventana()` |
| `window_width()` | `ancho_la_ventana()` | `ancho_la_ventana()` |
| `back()` | `atrás()` | `atras()` |
| `begin_fill()` | `comenzar_rellenar()` | `comenzar_rellenar()` |
| `begin_poly()` | `comenzar_polígono()` | `comenzar_poligono()` |
| `circle()` | `círculo()` | `circulo()` |
| `clear()` | `borrar()` | `borrar()` |
| `clearstamp()` | `borrar_sello()` | `borrar_sello()` |
| `clearstamps()` | `borrar_todos_sellos()` | `borrar_todos_sellos()` |
| `clone()` | `clonar()` | `clonar()` |
| `color()` | `configuración_color()` | `configuracion_color()` |
| `degrees()` | `grados()` | `grados()` |
| `distance()` | `distancia()` | `distancia()` |
| `dot()` | `punto()` | `punto()` |
| `end_fill()` | `terminar_relleno()` | `terminar_relleno()` |
| `end_poly()` | `terminar_polígono()` | `terminar_poligono()` |
| `fillcolor()` | `color_relleno()` | `color_relleno()` |
| `filling()` | `rellenando_ahora()` | `rellenando_ahora()` |
| `forward()` | `adelante()` | `adelante()` |
| `get_poly()` | `obtener_último_polígono()` | `obtener_ultimo_poligono()` |
| `getpen()` | `obtener_pluma()` | `obtener_pluma()` |
| `getscreen()` | `obtener_pantalla()` | `obtener_pantalla()` |
| `get_shapepoly()` | `obtener_polígono_forma()` | `obtener_poligono_forma()` |
| `getturtle()` | `obtener_tortuga()` | `obtener_tortuga()` |
| `goto()` | `ir_a()` | `ir_a()` |
| `heading()` | `dirección()` | `direccion()` |
| `hideturtle()` | `ocultar_tortuga()` | `ocultar_tortuga()` |
| `home()` | `origen()` | `origen()` |
| `isdown()` | `está_abajo()` | `esta_abajo()` |
| `isvisible()` | `es_visible()` | `es_visible()` |
| `left()` | `izquierda()` | `izquierda()` |
| `onclick()` | `al_hacer_clic()` | `al_hacer_clic()` |
| `ondrag()` | `al_arrastrar()` | `al_arrastrar()` |
| `onrelease()` | `al_soltar()` | `al_soltar()` |
| `pen()` | `configuración_pluma()` | `configuracion_pluma()` |
| `pencolor()` | `color_pluma()` | `color_pluma()` |
| `pendown()` | `pluma_abajo()` | `pluma_abajo()` |
| `pensize()` | `tamaño_pluma()` | `tamano_pluma()` |
| `penup()` | `pluma_arriba()` | `pluma_arriba()` |
| `position()` | `posición()` | `posicion()` |
| `radians()` | `radianes()` | `radianes()` |
| `right()` | `derecha()` | `derecha()` |
| `reset()` | `reiniciar_pantalla()` | `reiniciar_pantalla()` |
| `resizemode()` | `modo_cambio_tamaño()` | `modo_cambio_tamano()` |
| `setheading()` | `establecer_dirección()` | `establecer_direccion()` |
| `setundobuffer()` | `establecer_búfer_deshacer()` | `establecer_bufer_deshacer()` |
| `setx()` | `establecer_x()` | `establecer_x()` |
| `sety()` | `establecer_y()` | `establecer_y()` |
| `shape()` | `forma()` | `forma()` |
| `shapesize()` | `tamaño_forma()` | `tamano_forma()` |
| `shapetransform()` | `transformación_forma()` | `transformacion_forma()` |
| `shearfactor()` | `factor_cizalladura()` | `factor_cizalladura()` |
| `showturtle()` | `mostrar_tortuga()` | `mostrar_tortuga()` |
| `speed()` | `velocidad()` | `velocidad()` |
| `stamp()` | `sello()` | `sello()` |
| `teleport()` | `teletransportar()` | `teletransportar()` |
| `tilt()` | `rotar_cursor()` | `rotar_cursor()` |
| `tiltangle()` | `rotar_cursor_hacia()` | `rotar_cursor_hacia()` |
| `towards()` | `hacia()` | `hacia()` |
| `undo()` | `deshacer()` | `deshacer()` |
| `undobufferentries()` | `entradas_búfer_deshacer()` | `entradas_bufer_deshacer()` |
| `write()` | `escribir()` | `escribir()` |
| `xcor()` | `posición_x()` | `posicion_x()` |
| `ycor()` | `posición_y()` | `posicion_y()` |
| `picname` | `nombre_del_archivo` | `nombre_del_archivo` |
| `cmode` | `modo_color` | `modo_color` |
| `xdummy` | `ignorar_x` | `ignorar_x` |
| `ydummy` | `ignorar_y` | `ignorar_y` |
| `prompt` | `mensaje` | `mensaje` |
| `default` | `predeterminado` | `predeterminado` |
| `minval` | `valor_mínimo` | `valor_minimo` |
| `maxval` | `valor_máximo` | `valor_maximo` |
| `filename` | `nombre_de_archivo` | `nombre_de_archivo` |
| `overwrite` | `sobrescribir` | `sobrescribir` |
| `fun` | `función` | `funcion` |
| `key` | `tecla_teclado` | `tecla_teclado` |
| `btn` | `botón` | `boton` |
| `add` | `agregar_forma` | `agregar_forma` |
| `canvwidth` | `ancho_lienzo` | `ancho_lienzo` |
| `canvheight` | `altura_lienzo` | `altura_lienzo` |
| `bg` | `fondo` | `fondo` |
| `width` | `ancho` | `ancho` |
| `height` | `alto` | `alto` |
| `startx` | `inicio_x` | `inicio_x` |
| `starty` | `inicio_y` | `inicio_y` |
| `llx` | `x_inferior_izquierda` | `x_inferior_izquierda` |
| `lly` | `y_inferior_izquierda` | `y_inferior_izquierda` |
| `urx` | `x_superior_derecha` | `x_superior_derecha` |
| `ury` | `y_superior_derecha` | `y_superior_derecha` |
| `titlestring` | `título` | `titulo` |
| `radius` | `radio` | `radio` |
| `extent` | `tamaño_arco` | `tamano_arco` |
| `steps` | `pasos` | `pasos` |
| `stampid` | `ID_sello` | `ID_sello` |
| `fullcircle` | `círculo_completo` | `circulo_completo` |
| `size` | `tamaño` | `tamano` |
| `pendict` | `parámetros_bolígrafo` | `parametros_bolígrafo` |
| `angle` | `ángulo` | `angulo` |
| `rmode` | `modo_cambio_tamaño` | `modo_cambio_tamano` |
| `to_angle` | `ángulo` | `angulo` |
| `name` | `nombre` | `nombre` |
| `stretch_wid` | `ancho_estiramiento` | `ancho_estiramiento` |
| `stretch_len` | `longitud_estiramiento` | `longitud_estiramiento` |
| `outline` | `contorno` | `contorno` |
| `shear` | `cizalladura` | `cizalladura` |
| `fill_gap` | `hueco_relleno` | `hueco_relleno` |
| `move` | `mover` | `mover` |
| `align` | `alinear` | `alinear` |
| `font` | `fuente` | `fuente` |
| `'black'` | `'negro'` | `'negro'` |
| `'blue'` | `'azul'` | `'azul'` |
| `'brown'` | `'marrón'` | `'marron'` |
| `'orange'` | `'naranja'` | `'naranja'` |
| `'gray'` | `'gris'` | `'gris'` |
| `'grey'` | `'gris'` | `'gris'` |
| `'green'` | `'verde'` | `'verde'` |
| `'purple'` | `'morado'` | `'morado'` |
| `'violet'` | `'violeta'` | `'violeta'` |
| `'pink'` | `'rosa'` | `'rosa'` |
| `'yellow'` | `'amarillo'` | `'amarillo'` |
| `'white'` | `'blanco'` | `'blanco'` |
| `'red'` | `'rojo'` | `'rojo'` |
| `'magenta'` | `'magenta'` | `'magenta'` |
| `'cyan'` | `'cian'` | `'cian'` |
| `'arrow'` | `'flecha'` | `'flecha'` |
| `'blank'` | `'vacío'` | `'vacio'` |
| `'classic'` | `'clásico'` | `'clasico'` |
| `'square'` | `'cuadrado'` | `'cuadrado'` |
| `'triangle'` | `'triángulo'` | `'triangulo'` |
| `'turtle'` | `'tortuga'` | `'tortuga'` |
| `'polygon'` | `'polígono'` | `'poligono'` |
| `'image'` | `'imagen'` | `'imagen'` |
| `'compound'` | `'compuesto'` | `'compuesto'` |
| `'center'` | `'centro'` | `'centro'` |
| `'nopic'` | `'nada'` | `'nada'` |
| `'fastest'` | `'más_rápida'` | `'mas_rapida'` |
| `'fast'` | `'rápida'` | `'rapida'` |
| `'normal'` | `'normal'` | `'normal'` |
| `'slow'` | `'lenta'` | `'lenta'` |
| `'slowest'` | `'más_lenta'` | `'mas_lenta'` |
| `'shown'` | `'visible'` | `'visible'` |
| `'standard'` | `'normal'` | `'normal'` |
| `'logo'` | `'logo'` | `'logo'` |
| `'world'` | `'mundo'` | `'mundo'` |
| `'bold'` | `'negrita'` | `'negrita'` |
| `'italic'` | `'cursiva'` | `'cursiva'` |
| `'underline'` | `'subrayada'` | `'subrayada'` |

### Français/French

| English | French | French ASCII |
| --- | --- | --- |
| `bgcolor()` | `couleur_fond()` | `couleur_fond()` |
| `bgpic()` | `image_fond()` | `image_fond()` |
| `bye()` | `au_revoir()` | `au_revoir()` |
| `clearscreen()` | `effacer_écran()` | `effacer_ecran()` |
| `colormode()` | `mode_couleur()` | `mode_couleur()` |
| `delay()` | `délai()` | `delai()` |
| `done()` | `faite()` | `faite()` |
| `exitonclick()` | `quitter_au_clic()` | `quitter_au_clic()` |
| `getcanvas()` | `obtenir_toile()` | `obtenir_toile()` |
| `getshapes()` | `obtenir_formes()` | `obtenir_formes()` |
| `listen()` | `fenêtre_focus()` | `fenetre_focus()` |
| `mainloop()` | `boucle_principale()` | `boucle_principale()` |
| `mode()` | `mode_tortue()` | `mode_tortue()` |
| `no_animation()` | `pas_animation()` | `pas_animation()` |
| `numinput()` | `entrer_un_nombre()` | `entrer_un_nombre()` |
| `onkey()` | `sur_touche()` | `sur_touche()` |
| `onkeypress()` | `à_pression_touche()` | `a_pression_touche()` |
| `onkeyrelease()` | `au_relâchement_touche()` | `au_relachement_touche()` |
| `onscreenclick()` | `au_clic_sur_écran()` | `au_clic_sur_ecran()` |
| `ontimer()` | `sur_minuterie()` | `sur_minuterie()` |
| `register_shape()` | `ajouter_une_forme()` | `ajouter_une_forme()` |
| `resetscreen()` | `réinitialiser_écran()` | `reinitialiser_ecran()` |
| `save()` | `sauvegarder()` | `sauvegarder()` |
| `screensize()` | `taille_écran()` | `taille_ecran()` |
| `setup()` | `configuration()` | `configuration()` |
| `setworldcoordinates()` | `définir_coordonnées_monde()` | `definir_coordonnees_monde()` |
| `textinput()` | `entrer_texte()` | `entrer_texte()` |
| `title()` | `titre()` | `titre()` |
| `tracer()` | `taux_dessin()` | `taux_dessin()` |
| `turtles()` | `tortues()` | `tortues()` |
| `update()` | `mettre_à_jour()` | `mettre_a_jour()` |
| `window_height()` | `hauteur_fenêtre()` | `hauteur_fenetre()` |
| `window_width()` | `largeur_fenêtre()` | `largeur_fenetre()` |
| `back()` | `reculer()` | `reculer()` |
| `begin_fill()` | `commencer_remplissage()` | `commencer_remplissage()` |
| `begin_poly()` | `commencer_polygone()` | `commencer_polygone()` |
| `circle()` | `cercle()` | `cercle()` |
| `clear()` | `effacer()` | `effacer()` |
| `clearstamp()` | `effacer_tampon()` | `effacer_tampon()` |
| `clearstamps()` | `effacer_tous_tampons()` | `effacer_tous_tampons()` |
| `clone()` | `cloner()` | `cloner()` |
| `color()` | `couleur()` | `couleur()` |
| `degrees()` | `degrés()` | `degres()` |
| `distance()` | `distance_à()` | `distance_a()` |
| `dot()` | `point()` | `point()` |
| `end_fill()` | `terminer_remplissage()` | `terminer_remplissage()` |
| `end_poly()` | `terminer_polygone()` | `terminer_polygone()` |
| `fillcolor()` | `couleur_remplissage()` | `couleur_remplissage()` |
| `filling()` | `remplissage_en_cours()` | `remplissage_en_cours()` |
| `forward()` | `avancer()` | `avancer()` |
| `get_poly()` | `obtenir_dernier_polygone()` | `obtenir_dernier_polygone()` |
| `getpen()` | `obtenir_stylo()` | `obtenir_stylo()` |
| `getscreen()` | `obtenir_écran()` | `obtenir_ecran()` |
| `get_shapepoly()` | `obtenir_polygone_forme()` | `obtenir_polygone_forme()` |
| `getturtle()` | `obtenir_tortue()` | `obtenir_tortue()` |
| `goto()` | `aller_à()` | `aller_a()` |
| `heading()` | `direction()` | `direction()` |
| `hideturtle()` | `cacher_tortue()` | `cacher_tortue()` |
| `home()` | `origine()` | `origine()` |
| `isdown()` | `est_abaissé()` | `est_abaisse()` |
| `isvisible()` | `est_visible()` | `est_visible()` |
| `left()` | `gauche()` | `gauche()` |
| `onclick()` | `au_clic()` | `au_clic()` |
| `ondrag()` | `au_glisser()` | `au_glisser()` |
| `onrelease()` | `au_relâchement()` | `au_relachement()` |
| `pen()` | `paramètres_stylo()` | `parametres_stylo()` |
| `pencolor()` | `couleur_du_stylo()` | `couleur_du_stylo()` |
| `pendown()` | `stylo_en_bas()` | `stylo_en_bas()` |
| `pensize()` | `taille_stylo()` | `taille_stylo()` |
| `penup()` | `stylo_en_haut()` | `stylo_en_haut()` |
| `position()` | `coordonnées()` | `coordonnees()` |
| `radians()` | `mode_radians()` | `mode_radians()` |
| `right()` | `droite()` | `droite()` |
| `reset()` | `réinitialiser_écran()` | `reinitialiser_ecran()` |
| `resizemode()` | `mode_redimensionnement()` | `mode_redimensionnement()` |
| `setheading()` | `définir_direction()` | `definir_direction()` |
| `setundobuffer()` | `définir_tampon_annulation()` | `definir_tampon_annulation()` |
| `setx()` | `définir_x()` | `definir_x()` |
| `sety()` | `définir_y()` | `definir_y()` |
| `shape()` | `forme()` | `forme()` |
| `shapesize()` | `taille_forme()` | `taille_forme()` |
| `shapetransform()` | `transformation_forme()` | `transformation_forme()` |
| `shearfactor()` | `facteur_cisaillement()` | `facteur_cisaillement()` |
| `showturtle()` | `montrer_tortue()` | `montrer_tortue()` |
| `speed()` | `vitesse()` | `vitesse()` |
| `stamp()` | `tampon()` | `tampon()` |
| `teleport()` | `téléporter()` | `teleporter()` |
| `tilt()` | `faire_pivoter_curseur()` | `faire_pivoter_curseur()` |
| `tiltangle()` | `orienter_curseur_vers()` | `orienter_curseur_vers()` |
| `towards()` | `vers()` | `vers()` |
| `undo()` | `annuler()` | `annuler()` |
| `undobufferentries()` | `entrées_tampon_annulation()` | `entrees_tampon_annulation()` |
| `write()` | `écrire()` | `ecrire()` |
| `xcor()` | `position_x()` | `position_x()` |
| `ycor()` | `position_y()` | `position_y()` |
| `picname` | `nom_de_fichier` | `nom_de_fichier` |
| `cmode` | `mode_couleur` | `mode_couleur` |
| `xdummy` | `ignorer_x` | `ignorer_x` |
| `ydummy` | `ignorer_y` | `ignorer_y` |
| `prompt` | `message` | `message` |
| `default` | `par_défaut` | `par_defaut` |
| `minval` | `valeur_minimale` | `valeur_minimale` |
| `maxval` | `valeur_maximale` | `valeur_maximale` |
| `filename` | `nom_de_fichier` | `nom_de_fichier` |
| `overwrite` | `écraser` | `ecraser` |
| `fun` | `fonction` | `fonction` |
| `key` | `touche_clavier` | `touche_clavier` |
| `btn` | `bouton` | `bouton` |
| `add` | `ajouter_une_forme` | `ajouter_une_forme` |
| `canvwidth` | `largeur_toile` | `largeur_toile` |
| `canvheight` | `hauteur_toile` | `hauteur_toile` |
| `bg` | `arrière_plan` | `arriere_plan` |
| `width` | `largeur` | `largeur` |
| `height` | `hauteur` | `hauteur` |
| `startx` | `début_x` | `debut_x` |
| `starty` | `début_y` | `debut_y` |
| `llx` | `bas_gauche_x` | `bas_gauche_x` |
| `lly` | `bas_gauche_y` | `bas_gauche_y` |
| `urx` | `haut_droit_x` | `haut_droit_x` |
| `ury` | `haut_droit_y` | `haut_droit_y` |
| `titlestring` | `titre` | `titre` |
| `radius` | `rayon` | `rayon` |
| `extent` | `taille_arc` | `taille_arc` |
| `steps` | `étapes` | `etapes` |
| `stampid` | `ID_tampon` | `ID_tampon` |
| `fullcircle` | `cercle_complet` | `cercle_complet` |
| `size` | `taille` | `taille` |
| `pendict` | `paramètres_du_stylo` | `parametres_du_stylo` |
| `angle` | `angle` | `angle` |
| `rmode` | `mode_redimensionnement` | `mode_redimensionnement` |
| `to_angle` | `angle` | `angle` |
| `name` | `nom` | `nom` |
| `stretch_wid` | `étirer_largeur` | `etirer_largeur` |
| `stretch_len` | `étirer_longueur` | `etirer_longueur` |
| `outline` | `contour` | `contour` |
| `shear` | `cisaillement` | `cisaillement` |
| `fill_gap` | `écart_remplissage` | `ecart_remplissage` |
| `move` | `déplacer` | `deplacer` |
| `align` | `aligner` | `aligner` |
| `font` | `fonte` | `fonte` |
| `'black'` | `'noir'` | `'noir'` |
| `'blue'` | `'bleu'` | `'bleu'` |
| `'brown'` | `'brun'` | `'brun'` |
| `'orange'` | `'orange'` | `'orange'` |
| `'gray'` | `'gris'` | `'gris'` |
| `'grey'` | `'gris'` | `'gris'` |
| `'green'` | `'vert'` | `'vert'` |
| `'purple'` | `'violet'` | `'violet'` |
| `'violet'` | `'violet'` | `'violet'` |
| `'pink'` | `'rose'` | `'rose'` |
| `'yellow'` | `'jaune'` | `'jaune'` |
| `'white'` | `'blanc'` | `'blanc'` |
| `'red'` | `'rouge'` | `'rouge'` |
| `'magenta'` | `'magenta'` | `'magenta'` |
| `'cyan'` | `'cyan'` | `'cyan'` |
| `'arrow'` | `'flèche'` | `'fleche'` |
| `'blank'` | `'vide'` | `'vide'` |
| `'classic'` | `'classique'` | `'classique'` |
| `'square'` | `'carré'` | `'carre'` |
| `'triangle'` | `'triangle'` | `'triangle'` |
| `'turtle'` | `'tortue'` | `'tortue'` |
| `'polygon'` | `'polygone'` | `'polygone'` |
| `'image'` | `'image'` | `'image'` |
| `'compound'` | `'composé'` | `'compose'` |
| `'center'` | `'centre'` | `'centre'` |
| `'nopic'` | `'rien'` | `'rien'` |
| `'fastest'` | `'plus_rapide'` | `'plus_rapide'` |
| `'fast'` | `'rapide'` | `'rapide'` |
| `'normal'` | `'normale'` | `'normale'` |
| `'slow'` | `'lente'` | `'lente'` |
| `'slowest'` | `'plus_lente'` | `'plus_lente'` |
| `'shown'` | `'visible'` | `'visible'` |
| `'standard'` | `'normale'` | `'normale'` |
| `'logo'` | `'logo'` | `'logo'` |
| `'world'` | `'monde'` | `'monde'` |
| `'bold'` | `'gras'` | `'gras'` |
| `'italic'` | `'italique'` | `'italique'` |
| `'underline'` | `'soulignement'` | `'soulignement'` |

### Deutsch/German

| English | German | German ASCII |
| --- | --- | --- |
| `bgcolor()` | `Hintergrundfarbe()` | `Hintergrundfarbe()` |
| `bgpic()` | `Hintergrundbild()` | `Hintergrundbild()` |
| `bye()` | `Tschüss()` | `Tschuess()` |
| `clearscreen()` | `Bildschirm_löschen()` | `Bildschirm_loeschen()` |
| `colormode()` | `Farbmodus()` | `Farbmodus()` |
| `delay()` | `Verzögerung()` | `Verzoegerung()` |
| `done()` | `fertiggestellt()` | `fertiggestellt()` |
| `exitonclick()` | `Beenden_bei_Klick()` | `Beenden_bei_Klick()` |
| `getcanvas()` | `Leinwand_abrufen()` | `Leinwand_abrufen()` |
| `getshapes()` | `Formen_abrufen()` | `Formen_abrufen()` |
| `listen()` | `Fenster_fokussieren()` | `Fenster_fokussieren()` |
| `mainloop()` | `Hauptschleife()` | `Hauptschleife()` |
| `mode()` | `Modus()` | `Modus()` |
| `no_animation()` | `keine_Animation()` | `keine_Animation()` |
| `numinput()` | `Zahl_eingeben()` | `Zahl_eingeben()` |
| `onkey()` | `Bei_Taste()` | `Bei_Taste()` |
| `onkeypress()` | `Bei_Tastendruck()` | `Bei_Tastendruck()` |
| `onkeyrelease()` | `Bei_Tastenfreigabe()` | `Bei_Tastenfreigabe()` |
| `onscreenclick()` | `Bei_Bildschirmklick()` | `Bei_Bildschirmklick()` |
| `ontimer()` | `Bei_Timer()` | `Bei_Timer()` |
| `register_shape()` | `Form_hinzufügen()` | `Form_hinzufuegen()` |
| `resetscreen()` | `Bildschirm_zurücksetzen()` | `Bildschirm_zuruecksetzen()` |
| `save()` | `speichern()` | `speichern()` |
| `screensize()` | `Bildschirmgröße()` | `Bildschirmgroesse()` |
| `setup()` | `Einrichten()` | `Einrichten()` |
| `setworldcoordinates()` | `Weltkoordinaten_setzen()` | `Weltkoordinaten_setzen()` |
| `textinput()` | `Text_eingeben()` | `Text_eingeben()` |
| `title()` | `Titel()` | `Titel()` |
| `tracer()` | `Zeichengeschwindigkeit()` | `Zeichengeschwindigkeit()` |
| `turtles()` | `Schildkröten()` | `Schildkroeten()` |
| `update()` | `Aktualisieren()` | `Aktualisieren()` |
| `window_height()` | `Fensterhöhe()` | `Fensterhoehe()` |
| `window_width()` | `Fensterbreite()` | `Fensterbreite()` |
| `back()` | `Rückwärts()` | `Rueckwaerts()` |
| `begin_fill()` | `Füllen_beginnen()` | `Fuellen_beginnen()` |
| `begin_poly()` | `Polygon_beginnen()` | `Polygon_beginnen()` |
| `circle()` | `Kreis()` | `Kreis()` |
| `clear()` | `Löschen()` | `Loeschen()` |
| `clearstamp()` | `Stempel_löschen()` | `Stempel_loeschen()` |
| `clearstamps()` | `Alle_Stempel_löschen()` | `Alle_Stempel_loeschen()` |
| `clone()` | `Klonen()` | `Klonen()` |
| `color()` | `Farbe()` | `Farbe()` |
| `degrees()` | `Grad()` | `Grad()` |
| `distance()` | `Distanz()` | `Distanz()` |
| `dot()` | `Punkt()` | `Punkt()` |
| `end_fill()` | `Füllen_beenden()` | `Fuellen_beenden()` |
| `end_poly()` | `Polygon_beenden()` | `Polygon_beenden()` |
| `fillcolor()` | `Füllfarbe()` | `Fuellfarbe()` |
| `filling()` | `Gerade_füllen()` | `Gerade_fuellen()` |
| `forward()` | `Vorwärts()` | `Vorwaerts()` |
| `get_poly()` | `Letztes_Polygon_abrufen()` | `Letztes_Polygon_abrufen()` |
| `getpen()` | `Stift_abrufen()` | `Stift_abrufen()` |
| `getscreen()` | `Bildschirm_abrufen()` | `Bildschirm_abrufen()` |
| `get_shapepoly()` | `Formpolygon_abrufen()` | `Formpolygon_abrufen()` |
| `getturtle()` | `Schildkröte_abrufen()` | `Schildkroete_abrufen()` |
| `goto()` | `Gehe_zu()` | `Gehe_zu()` |
| `heading()` | `Richtung()` | `Richtung()` |
| `hideturtle()` | `Schildkröte_verstecken()` | `Schildkroete_verstecken()` |
| `home()` | `Ursprung()` | `Ursprung()` |
| `isdown()` | `Ist_unten()` | `Ist_unten()` |
| `isvisible()` | `Ist_sichtbar()` | `Ist_sichtbar()` |
| `left()` | `Links()` | `Links()` |
| `onclick()` | `Bei_Klick()` | `Bei_Klick()` |
| `ondrag()` | `Beim_Ziehen()` | `Beim_Ziehen()` |
| `onrelease()` | `Bei_Freigabe()` | `Bei_Freigabe()` |
| `pen()` | `Stifteinstellung()` | `Stifteinstellung()` |
| `pencolor()` | `Stiftfarbe()` | `Stiftfarbe()` |
| `pendown()` | `Stift_nach_unten()` | `Stift_nach_unten()` |
| `pensize()` | `Stiftdicke()` | `Stiftdicke()` |
| `penup()` | `Stift_nach_oben()` | `Stift_nach_oben()` |
| `position()` | `Position()` | `Position()` |
| `radians()` | `Bogenmaß()` | `Bogenmass()` |
| `right()` | `Rechts()` | `Rechts()` |
| `reset()` | `Bildschirm_zurücksetzen()` | `Bildschirm_zuruecksetzen()` |
| `resizemode()` | `Größenmodus()` | `Groessenmodus()` |
| `setheading()` | `Richtung_setzen()` | `Richtung_setzen()` |
| `setundobuffer()` | `Rückgangepuffer_setzen()` | `Rueckgangepuffer_setzen()` |
| `setx()` | `X_setzen()` | `X_setzen()` |
| `sety()` | `Y_setzen()` | `Y_setzen()` |
| `shape()` | `Form()` | `Form()` |
| `shapesize()` | `Formgröße()` | `Formgroesse()` |
| `shapetransform()` | `Formtransformation()` | `Formtransformation()` |
| `shearfactor()` | `Scherspannung()` | `Scherspannung()` |
| `showturtle()` | `Schildkröte_zeigen()` | `Schildkroete_zeigen()` |
| `speed()` | `Geschwindigkeit()` | `Geschwindigkeit()` |
| `stamp()` | `Stempeln()` | `Stempeln()` |
| `teleport()` | `Teleportieren()` | `Teleportieren()` |
| `tilt()` | `Cursor_drehen()` | `Cursor_drehen()` |
| `tiltangle()` | `Cursor_drehen_zu()` | `Cursor_drehen_zu()` |
| `towards()` | `Zu()` | `Zu()` |
| `undo()` | `Rückgängig()` | `Rueckgaengig()` |
| `undobufferentries()` | `Rückgangepuffer_Einträge()` | `Rueckgangepuffer_Eintraege()` |
| `write()` | `Schreiben()` | `Schreiben()` |
| `xcor()` | `X_Position()` | `X_Position()` |
| `ycor()` | `Y_Position()` | `Y_Position()` |
| `picname` | `Dateiname` | `Dateiname` |
| `cmode` | `Farbmodus` | `Farbmodus` |
| `xdummy` | `X_ignorieren` | `X_ignorieren` |
| `ydummy` | `Y_ignorieren` | `Y_ignorieren` |
| `prompt` | `Nachricht` | `Nachricht` |
| `default` | `Standard` | `Standard` |
| `minval` | `Mindestwert` | `Mindestwert` |
| `maxval` | `Höchstwert` | `Hoechstwert` |
| `filename` | `Dateiname` | `Dateiname` |
| `overwrite` | `überschreiben` | `ueberschreiben` |
| `fun` | `Funktion` | `Funktion` |
| `key` | `Tastaturtaste` | `Tastaturtaste` |
| `btn` | `Schaltfläche` | `Schaltflaeche` |
| `add` | `Form_hinzufügen` | `Form_hinzufuegen` |
| `canvwidth` | `Leinwandbreite` | `Leinwandbreite` |
| `canvheight` | `Leinwandhöhe` | `Leinwandhoehe` |
| `bg` | `Hintergrund` | `Hintergrund` |
| `width` | `Breite` | `Breite` |
| `height` | `Höhe` | `Hoehe` |
| `startx` | `Start_X` | `Start_X` |
| `starty` | `Start_Y` | `Start_Y` |
| `llx` | `Unten_links_X` | `Unten_links_X` |
| `lly` | `Unten_links_Y` | `Unten_links_Y` |
| `urx` | `Oben_rechts_X` | `Oben_rechts_X` |
| `ury` | `Oben_rechts_Y` | `Oben_rechts_Y` |
| `titlestring` | `Titel` | `Titel` |
| `radius` | `Radius` | `Radius` |
| `extent` | `Bogenmaß` | `Bogenmass` |
| `steps` | `Schritte` | `Schritte` |
| `stampid` | `Stempel_ID` | `Stempel_ID` |
| `fullcircle` | `Vollkreis` | `Vollkreis` |
| `size` | `Größe` | `Groesse` |
| `pendict` | `Stiftparameter` | `Stiftparameter` |
| `angle` | `Winkel` | `Winkel` |
| `rmode` | `Größenmodus` | `Groessenmodus` |
| `to_angle` | `Winkel` | `Winkel` |
| `name` | `Name` | `Name` |
| `stretch_wid` | `Streckbreite` | `Streckbreite` |
| `stretch_len` | `Strecklänge` | `Strecklaenge` |
| `outline` | `Umriss` | `Umriss` |
| `shear` | `Schub` | `Schub` |
| `fill_gap` | `Fülllücke` | `Fuellluecke` |
| `move` | `Bewegen` | `Bewegen` |
| `align` | `Ausrichten` | `Ausrichten` |
| `font` | `Schriftart` | `Schriftart` |
| `'black'` | `'Schwarz'` | `'Schwarz'` |
| `'blue'` | `'Blau'` | `'Blau'` |
| `'brown'` | `'Braun'` | `'Braun'` |
| `'orange'` | `'Orange'` | `'Orange'` |
| `'gray'` | `'Grau'` | `'Grau'` |
| `'grey'` | `'Grau'` | `'Grau'` |
| `'green'` | `'Grün'` | `'Gruen'` |
| `'purple'` | `'Lila'` | `'Lila'` |
| `'violet'` | `'Violett'` | `'Violett'` |
| `'pink'` | `'Rosa'` | `'Rosa'` |
| `'yellow'` | `'Gelb'` | `'Gelb'` |
| `'white'` | `'Weiß'` | `'Weiss'` |
| `'red'` | `'Rot'` | `'Rot'` |
| `'magenta'` | `'Magenta'` | `'Magenta'` |
| `'cyan'` | `'Cyan'` | `'Cyan'` |
| `'arrow'` | `'Pfeil'` | `'Pfeil'` |
| `'blank'` | `'Leer'` | `'Leer'` |
| `'classic'` | `'Klassisch'` | `'Klassisch'` |
| `'square'` | `'Quadrat'` | `'Quadrat'` |
| `'triangle'` | `'Dreieck'` | `'Dreieck'` |
| `'turtle'` | `'Schildkröte'` | `'Schildkroete'` |
| `'polygon'` | `'Polygon'` | `'Polygon'` |
| `'image'` | `'Bild'` | `'Bild'` |
| `'compound'` | `'Verbund'` | `'Verbund'` |
| `'center'` | `'Zentrum'` | `'Zentrum'` |
| `'nopic'` | `'Nichts'` | `'Nichts'` |
| `'fastest'` | `'schnellste'` | `'schnellste'` |
| `'fast'` | `'schnelle'` | `'schnelle'` |
| `'normal'` | `'normale'` | `'normale'` |
| `'slow'` | `'langsame'` | `'langsame'` |
| `'slowest'` | `'langsamste'` | `'langsamste'` |
| `'shown'` | `'sichtbar'` | `'sichtbar'` |
| `'standard'` | `'Normal'` | `'Normal'` |
| `'logo'` | `'logo'` | `'logo'` |
| `'world'` | `'Welt'` | `'Welt'` |
| `'bold'` | `'fett'` | `'fett'` |
| `'italic'` | `'kursive'` | `'kursive'` |
| `'underline'` | `'unterstreichung'` | `'unterstreichung'` |

The string arguments to the `speed()` function (and its non-English functions) are:

| English | `'fastest'` | `'fast'` | `'regular'` | `'slow'` | `'slowest'` |
| --- | --- | --- | --- | --- | --- |
| Spanish | `'más rápida'` | `'rápida'` | `'normal'` | `'lenta'` | `'más lenta'` |
| Spanish ASCII | `'mas rapida'` | `'rapida'` | `'normal'` | `'lenta'` | `'mas lenta'` |
| French, French ASCII | `'la plus rapide'` | `'rapide'` | `'normale'` | `'lente'` | `'la plus lente'` |
| German, German ASCII | `'schnellste'` | `'schnelle'` | `'normale'` | `'langsame'` | `'langsamste'` |


## Special Thanks To

* Gregor Lingl for his work on the original turtle.py module.
* Ari Lacenski for the Spanish translation
* Seunghyo Seo for the Korean translation
* Brian Ward and Catherine Devlin for the German translation
* Onur Ozay and Erman Korkut for the Turkish translation

