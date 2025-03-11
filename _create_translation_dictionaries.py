'''

Huh. This person says that, for French, I can cut out the "de" and "l'" and even accent marks. https://bsky.app/profile/did:plc:vuqnaifkj5ucl6vrrnhwz5e4/post/3lgz7yqzdr22w


'''


#_ENGLISH_IDENTIFIERS = ['bgcolor', 'bgpic', 'bye', 'clearscreen', 'colormode', 'delay', 'exitonclick', 'getcanvas', 'getshapes', 'listen', 'mainloop', 'mode', 'no_animation', 'numinput', 'onkey', 'onkeypress', 'onkeyrelease', 'onscreenclick', 'ontimer', 'register_shape', 'resetscreen', 'save', 'screensize', 'setup', 'setworldcoordinates', 'textinput', 'title', 'tracer', 'turtles', 'update', 'window_height', 'window_width', 'back', 'begin_fill', 'begin_poly', 'circle', 'clear', 'clearstamp', 'clearstamps', 'clone', 'color', 'degrees', 'distance', 'dot', 'end_fill', 'end_poly', 'fillcolor', 'filling', 'forward', 'get_poly', 'getpen', 'getscreen', 'get_shapepoly', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'isdown', 'isvisible', 'left', 'onclick', 'ondrag', 'onrelease', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'position', 'radians', 'right', 'reset', 'resizemode', 'setheading', 'setundobuffer', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle', 'speed', 'stamp', 'teleport', 'tilt', 'tiltangle', 'towards', 'undo', 'undobufferentries', 'write', 'xcor', 'ycor', 'picname', 'cmode', 'xdummy', 'ydummy', 'prompt', 'default', 'minval', 'maxval', 'filename', 'overwrite', 'fun', 'key', 'btn', 'add', 'canvwidth', 'canvheight', 'bg', 'width', 'height', 'startx', 'starty', 'llx', 'lly', 'urx', 'ury', 'titlestring', 'radius', 'extent', 'steps', 'stampid', 'fullcircle', 'size', 'pendict', 'angle', 'rmode', 'to_angle', 'name', 'stretch_wid', 'stretch_len', 'outline', 'shear', 'fill_gap', 'move', 'align', 'font', 'black', 'blue', 'brown', 'orange', 'gray', 'grey', 'green', 'purple', 'violet', 'pink', 'yellow', 'white', 'red', 'magenta', 'cyan', 'arrow', 'blank', 'classic', 'square', 'triangle', 'turtle', 'polygon', 'image', 'compound', 'center', 'nopic']

# This string value is copy/pasted from a spreadsheet for ease of updating:
_NUM_LANGUAGES = 7  # Update this as new languages are added to the spreadsheet.
_TRANSLATION_SPREADSHEET = '''\
bgcolor color_fondo color_fondo couleur_fond    couleur_fond    Hintergrundfarbe    Hintergrundfarbe
bgpic   imagen_fondo    imagen_fondo    image_fond  image_fond  Hintergrundbild Hintergrundbild
bye adiós   adios   au_revoir   au_revoir   Tschüss Tschuess
clearscreen borrar_pantalla borrar_pantalla effacer_écran   effacer_ecran   Bildschirm_löschen  Bildschirm_loeschen
colormode   modo_color  modo_color  mode_couleur    mode_couleur    Farbmodus   Farbmodus
delay   retraso retraso délai   delai   Verzögerung Verzoegerung
exitonclick salir_al_hacer_clic salir_al_hacer_clic quitter_au_clic quitter_au_clic Beenden_bei_Klick   Beenden_bei_Klick
getcanvas   obtener_lienzo  obtener_lienzo  obtenir_toile   obtenir_toile   Leinwand_abrufen    Leinwand_abrufen
getshapes   obtener_formas  obtener_formas  obtenir_formes  obtenir_formes  Formen_abrufen  Formen_abrufen
listen  enfocar_ventana enfocar_ventana fenêtre_focus   fenetre_focus   Fenster_fokussieren Fenster_fokussieren
mainloop    bucle_principal bucle_principal boucle_principale   boucle_principale   Hauptschleife   Hauptschleife
mode    modo    modo    mode    mode    Modus   Modus
no_animation    sin_animación   sin_animacion   pas_animation   pas_animation   keine_Animation keine_Animation
numinput    ingresar_número ingresar_numero entrer_un_nombre    entrer_un_nombre    Zahl_eingeben   Zahl_eingeben
onkey   al_presionar_tecla  al_presionar_tecla  sur_touche  sur_touche  Bei_Taste   Bei_Taste
onkeypress  al_pulsar_tecla al_pulsar_tecla à_pression_touche   a_pression_touche   Bei_Tastendruck Bei_Tastendruck
onkeyrelease    al_soltar_tecla al_soltar_tecla au_relâchement_touche   au_relachement_touche   Bei_Tastenfreigabe  Bei_Tastenfreigabe
onscreenclick   al_hacer_clic_en_pantalla   al_hacer_clic_en_pantalla   au_clic_sur_écran   au_clic_sur_ecran   Bei_Bildschirmklick Bei_Bildschirmklick
ontimer en_temporizador en_temporizador sur_minuterie   sur_minuterie   Bei_Timer   Bei_Timer
register_shape  agregar_forma   agregar_forma   ajouter_une_forme   ajouter_une_forme   Form_hinzufügen Form_hinzufuegen
resetscreen reiniciar_pantalla  reiniciar_pantalla  réinitialiser_écran reinitialiser_ecran Bildschirm_zurücksetzen Bildschirm_zuruecksetzen
save    ahorrar ahorrar sauvegarder sauvegarder speichern   speichern
screensize  tamaño_pantalla tamano_pantalla taille_écran    taille_ecran    Bildschirmgröße Bildschirmgroesse
setup   configurar  configurar  configuration   configuration   Einrichten  Einrichten
setworldcoordinates establecer_coordenadas_mundo    establecer_coordenadas_mundo    définir_coordonnées_monde   definir_coordonnees_monde   Weltkoordinaten_setzen  Weltkoordinaten_setzen
textinput   ingresar_texto  ingresar_texto  entrer_texte    entrer_texte    Text_eingeben   Text_eingeben
title   título  titulo  titre   titre   Titel   Titel
tracer  tasa_dibujo tasa_dibujo taux_dessin taux_dessin Zeichengeschwindigkeit  Zeichengeschwindigkeit
turtles tortugas    tortugas    tortues tortues Schildkröten    Schildkroeten
update  actualizar  actualizar  mettre_à_jour   mettre_a_jour   Aktualisieren   Aktualisieren
window_height   altura_la_ventana   altura_la_ventana   hauteur_fenêtre hauteur_fenetre Fensterhöhe Fensterhoehe
window_width    ancho_la_ventana    ancho_la_ventana    largeur_fenêtre largeur_fenetre Fensterbreite   Fensterbreite
back    atrás   atras   reculer reculer Rückwärts   Rueckwaerts
begin_fill  comenzar_a_rellenar comenzar_a_rellenar commencer_remplissage   commencer_remplissage   Füllen_beginnen Fuellen_beginnen
begin_poly  comenzar_polígono   comenzar_poligono   commencer_polygone  commencer_polygone  Polygon_beginnen    Polygon_beginnen
circle  círculo circulo cercle  cercle  Kreis   Kreis
clear   borrar  borrar  effacer effacer Löschen Loeschen
clearstamp  borrar_sello    borrar_sello    effacer_tampon  effacer_tampon  Stempel_löschen Stempel_loeschen
clearstamps borrar_todos_sellos borrar_todos_sellos effacer_tous_tampons    effacer_tous_tampons    Alle_Stempel_löschen    Alle_Stempel_loeschen
clone   clonar  clonar  cloner  cloner  Klonen  Klonen
color   color   color   couleur couleur Farbe   Farbe
degrees grados  grados  degrés  degres  Grad    Grad
distance    distancia   distancia   distance    distance    Distanz Distanz
dot punto   punto   point   point   Punkt   Punkt
end_fill    terminar_relleno    terminar_relleno    terminer_remplissage    terminer_remplissage    Füllen_beenden  Fuellen_beenden
end_poly    terminar_polígono   terminar_poligono   terminer_polygone   terminer_polygone   Polygon_beenden Polygon_beenden
fillcolor   color_relleno   color_relleno   couleur_remplissage couleur_remplissage Füllfarbe   Fuellfarbe
filling rellenando_ahora    rellenando_ahora    remplissage_en_cours    remplissage_en_cours    Gerade_füllen   Gerade_fuellen
forward adelante    adelante    avancer avancer Vorwärts    Vorwaerts
get_poly    obtener_último_polígono obtener_ultimo_poligono obtenir_dernier_polygone    obtenir_dernier_polygone    Letztes_Polygon_abrufen Letztes_Polygon_abrufen
getpen  obtener_pluma   obtener_pluma   obtenir_stylo   obtenir_stylo   Stift_abrufen   Stift_abrufen
getscreen   obtener_pantalla    obtener_pantalla    obtenir_écran   obtenir_ecran   Bildschirm_abrufen  Bildschirm_abrufen
get_shapepoly   obtener_polígono_forma  obtener_poligono_forma  obtenir_polygone_forme  obtenir_polygone_forme  Formpolygon_abrufen Formpolygon_abrufen
getturtle   obtener_tortuga obtener_tortuga obtenir_tortue  obtenir_tortue  Schildkröte_abrufen Schildkroete_abrufen
goto    ir_a    ir_a    aller_à aller_a Gehe_zu Gehe_zu
heading dirección   direccion   direction   direction   Richtung    Richtung
hideturtle  ocultar_tortuga ocultar_tortuga cacher_tortue   cacher_tortue   Schildkröte_verstecken  Schildkroete_verstecken
home    origen  origen  origine origine Ursprung    Ursprung
isdown  está_abajo  esta_abajo  est_abaissé est_abaisse Ist_unten   Ist_unten
isvisible   es_visible  es_visible  est_visible est_visible Ist_sichtbar    Ist_sichtbar
left    izquierda   izquierda   gauche  gauche  Links   Links
onclick al_hacer_clic   al_hacer_clic   au_clic au_clic Bei_Klick   Bei_Klick
ondrag  al_arrastrar    al_arrastrar    au_glisser  au_glisser  Beim_Ziehen Beim_Ziehen
onrelease   al_soltar   al_soltar   au_relâchement  au_relachement  Bei_Freigabe    Bei_Freigabe
pen pluma   pluma   stylo   stylo   Stift   Stift
pencolor    configuración_pluma configuracion_pluma paramètres_stylo    parametres_stylo    Stifteinstellung    Stifteinstellung
pendown pluma_abajo pluma_abajo stylo_en_bas    stylo_en_bas    Stift_nach_unten    Stift_nach_unten
pensize tamaño_pluma    tamano_pluma    taille_stylo    taille_stylo    Stiftdicke  Stiftdicke
penup   pluma_arriba    pluma_arriba    stylo_en_haut   stylo_en_haut   Stift_nach_oben Stift_nach_oben
position    posición    posicion    position    position    Position    Position
radians radianes    radianes    radians radians Bogenmaß    Bogenmass
right   derecha derecha droite  droite  Rechts  Rechts
reset   reiniciar_pantalla  reiniciar_pantalla  réinitialiser_écran reinitialiser_ecran Bildschirm_zurücksetzen Bildschirm_zuruecksetzen
resizemode  modo_cambio_tamaño  modo_cambio_tamano  mode_redimensionnement  mode_redimensionnement  Größenmodus Groessenmodus
setheading  establecer_dirección    establecer_direccion    définir_direction   definir_direction   Richtung_setzen Richtung_setzen
setundobuffer   establecer_búfer_deshacer   establecer_bufer_deshacer   définir_tampon_annulation   definir_tampon_annulation   Rückgangepuffer_setzen  Rueckgangepuffer_setzen
setx    establecer_x    establecer_x    définir_x   definir_x   X_setzen    X_setzen
sety    establecer_y    establecer_y    définir_y   definir_y   Y_setzen    Y_setzen
shape   forma   forma   forme   forme   Form    Form
shapesize   tamaño_forma    tamano_forma    taille_forme    taille_forme    Formgröße   Formgroesse
shapetransform  transformación_forma    transformacion_forma    transformation_forme    transformation_forme    Formtransformation  Formtransformation
shearfactor factor_cizalladura  factor_cizalladura  facteur_cisaillement    facteur_cisaillement    Scherspannung   Scherspannung
showturtle  mostrar_tortuga mostrar_tortuga montrer_tortue  montrer_tortue  Schildkröte_zeigen  Schildkroete_zeigen
speed   velocidad   velocidad   vitesse vitesse Geschwindigkeit Geschwindigkeit
stamp   sello   sello   tampon  tampon  Stempeln    Stempeln
teleport    teletransportar teletransportar téléporter  teleporter  Teleportieren   Teleportieren
tilt    rotar_cursor    rotar_cursor    faire_pivoter_curseur   faire_pivoter_curseur   Cursor_drehen   Cursor_drehen
tiltangle   rotar_cursor_hacia  rotar_cursor_hacia  orienter_curseur_vers   orienter_curseur_vers   Cursor_drehen_zu    Cursor_drehen_zu
towards hacia   hacia   vers    vers    Zu  Zu
undo    deshacer    deshacer    annuler annuler Rückgängig  Rueckgaengig
undobufferentries   entradas_búfer_deshacer entradas_bufer_deshacer entrées_tampon_annulation   entrees_tampon_annulation   Rückgangepuffer_Einträge    Rueckgangepuffer_Eintraege
write   escribir    escribir    écrire  ecrire  Schreiben   Schreiben
xcor    posición_x  posicion_x  position_x  position_x  X_Position  X_Position
ycor    posición_y  posicion_y  position_y  position_y  Y_Position  Y_Position
picname imagen  imagen  image   image   Bild    Bild
cmode   modo_color  modo_color  mode_couleur    mode_couleur    Farbmodus   Farbmodus
xdummy  ignorar_x   ignorar_x   ignorer_x   ignorer_x   X_ignorieren    X_ignorieren
ydummy  ignorar_y   ignorar_y   ignorer_y   ignorer_y   Y_ignorieren    Y_ignorieren
prompt  mensaje mensaje message message Nachricht   Nachricht
default predeterminado  predeterminado  par_défaut  par_defaut  Standard    Standard
minval  valor_mínimo    valor_minimo    valeur_minimale valeur_minimale Mindestwert Mindestwert
maxval  valor_máximo    valor_maximo    valeur_maximale valeur_maximale Höchstwert  Hoechstwert
filename    nombre_de_archivo   nombre_de_archivo   nom_de_fichier  nom_de_fichier  Dateiname   Dateiname
overwrite   sobrescribir    sobrescribir    écraser ecraser überschreiben   ueberschreiben
fun función funcion fonction    fonction    Funktion    Funktion
key tecla_teclado   tecla_teclado   touche_clavier  touche_clavier  Tastaturtaste   Tastaturtaste
btn botón   boton   bouton  bouton  Schaltfläche    Schaltflaeche
add agregar_forma   agregar_forma   ajouter_une_forme   ajouter_une_forme   Form_hinzufügen Form_hinzufuegen
canvwidth   ancho_lienzo    ancho_lienzo    largeur_toile   largeur_toile   Leinwandbreite  Leinwandbreite
canvheight  altura_lienzo   altura_lienzo   hauteur_toile   hauteur_toile   Leinwandhöhe    Leinwandhoehe
bg  fondo   fondo   arrière_plan    arriere_plan    Hintergrund Hintergrund
width   ancho   ancho   largeur largeur Breite  Breite
height  alto    alto    hauteur hauteur Höhe    Hoehe
startx  inicio_x    inicio_x    début_x debut_x Start_X Start_X
starty  inicio_y    inicio_y    début_y debut_y Start_Y Start_Y
llx x_inferior_izquierda    x_inferior_izquierda    bas_gauche_x    bas_gauche_x    Unten_links_X   Unten_links_X
lly y_inferior_izquierda    y_inferior_izquierda    bas_gauche_y    bas_gauche_y    Unten_links_Y   Unten_links_Y
urx x_superior_derecha  x_superior_derecha  haut_droit_x    haut_droit_x    Oben_rechts_X   Oben_rechts_X
ury y_superior_derecha  y_superior_derecha  haut_droit_y    haut_droit_y    Oben_rechts_Y   Oben_rechts_Y
titlestring título  titulo  titre   titre   Titel   Titel
radius  radio   radio   rayon   rayon   Radius  Radius
extent  extensión   extension   étendue etendue Bogenmaß    Bogenmass
steps   pasos   pasos   étapes  etapes  Schritte    Schritte
stampid ID_sello    ID_sello    ID_tampon   ID_tampon   Stempel_ID  Stempel_ID
fullcircle  círculo_completo    circulo_completo    cercle_complet  cercle_complet  Vollkreis   Vollkreis
size    tamaño  tamano  taille  taille  Größe   Groesse
pendict configuraciones_pluma   configuraciones_pluma   paramètres_stylo    parametres_stylo    Stifteinstellungen  Stifteinstellungen
angle   ángulo  angulo  angle   angle   Winkel  Winkel
rmode   modo_cambio_tamaño  modo_cambio_tamano  mode_redimensionnement  mode_redimensionnement  Größenmodus Groessenmodus
to_angle    ángulo  angulo  angle   angle   Winkel  Winkel
name    nombre  nombre  nom nom Name    Name
stretch_wid ancho_estiramiento  ancho_estiramiento  étirer_largeur  etirer_largeur  Streckbreite    Streckbreite
stretch_len longitud_estiramiento   longitud_estiramiento   étirer_longueur etirer_longueur Strecklänge Strecklaenge
outline contorno    contorno    contour contour Umriss  Umriss
shear   cizalladura cizalladura cisaillement    cisaillement    Schub   Schub
fill_gap    hueco_relleno   hueco_relleno   écart_remplissage   ecart_remplissage   Fülllücke   Fuellluecke
move    mover   mover   déplacer    deplacer    Bewegen Bewegen
align   alinear alinear aligner aligner Ausrichten  Ausrichten
font    fuente  fuente  police  police  Schriftart  Schriftart
black   negro   negro   noir    noir    Schwarz Schwarz
blue    azul    azul    bleu    bleu    Blau    Blau
brown   marrón  marron  brun    brun    Braun   Braun
orange  naranja naranja orange  orange  Orange  Orange
gray    gris    gris    gris    gris    Grau    Grau
grey    gris    gris    gris    gris    Grau    Grau
green   verde   verde   vert    vert    Grün    Gruen
purple  morado  morado  violet  violet  Lila    Lila
violet  violeta violeta violet  violet  Violett Violett
pink    rosa    rosa    rose    rose    Rosa    Rosa
yellow  amarillo    amarillo    jaune   jaune   Gelb    Gelb
white   blanco  blanco  blanc   blanc   Weiß    Weiss
red rojo    rojo    rouge   rouge   Rot Rot
magenta magenta magenta magenta magenta Magenta Magenta
cyan    cian    cian    cyan    cyan    Cyan    Cyan
arrow   flecha  flecha  flèche  fleche  Pfeil   Pfeil
blank   vacío   vacio   vide    vide    Leer    Leer
classic clásico clasico classique   classique   Klassisch   Klassisch
square  cuadrado    cuadrado    carré   carre   Quadrat Quadrat
triangle    triángulo   triangulo   triangle    triangle    Dreieck Dreieck
turtle  tortuga tortuga tortue  tortue  Schildkröte Schildkroete
polygon polígono    poligono    polygone    polygone    Polygon Polygon
image   imagen  imagen  image   image   Bild    Bild
compound    compuesto   compuesto   composé compose Verbund Verbund
center  centro  centro  centre  centre  Zentrum Zentrum
nopic   nada    nada    rien    rien    Nichts  Nichts'''.splitlines()


def _create_translation_dictionaries():
    global ES, ES_ASCII, FR, FR_ASCII, DE, DE_ASCII

    ES = {}
    ES_ASCII = {}
    FR = {}
    FR_ASCII = {}
    DE = {}
    DE_ASCII = {}

    for i, row in enumerate(_TRANSLATION_SPREADSHEET):
        assert '-' not in row, 'Dash character found in spreadsheet row: ' + row
        assert "'" not in row, 'Quote character found in spreadsheet row: ' + row

        spreadsheet_columns = row.split()

        assert len(spreadsheet_columns) == _NUM_LANGUAGES, 'Extra space found in spreadsheet row: ' + row

        english_identifier = spreadsheet_columns[0]

        ES[english_identifier] = spreadsheet_columns[1]
        ES_ASCII[english_identifier] = spreadsheet_columns[2]
        FR[english_identifier] = spreadsheet_columns[3]
        FR_ASCII[english_identifier] = spreadsheet_columns[4]
        DE[english_identifier] = spreadsheet_columns[5]
        DE_ASCII[english_identifier] = spreadsheet_columns[6]


_create_translation_dictionaries()
_ES_INVERSE = {v: k for k, v in ES.items()}
_ES_ASCII_INVERSE = {v: k for k, v in ES_ASCII.items()}
_FR_INVERSE = {v: k for k, v in FR.items()}
_FR_ASCII_INVERSE = {v: k for k, v in FR_ASCII.items()}
_DE_INVERSE = {v: k for k, v in DE.items()}
_DE_ASCII_INVERSE = {v: k for k, v in DE_ASCII.items()}


print(f'''
ES = {ES}
_ES_INVERSE = {{v: k for k, v in ES.items()}}

ES_ASCII = {ES_ASCII}
_ES_ASCII_INVERSE = {{v: k for k, v in ES_ASCII.items()}}

FR = {FR}
_FR_INVERSE = {{v: k for k, v in FR.items()}}

FR_ASCII = {FR_ASCII}
_FR_ASCII_INVERSE = {{v: k for k, v in FR_ASCII.items()}}

DE = {DE}
_DE_INVERSE = {{v: k for k, v in DE.items()}}

DE_ASCII = {DE_ASCII}
_DE_ASCII_INVERSE = {{v: k for k, v in DE_ASCII.items()}}
''')


