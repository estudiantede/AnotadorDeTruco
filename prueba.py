#Se importa TODAS las librerias
from guizero import *

def ganoPartida(participanteGanador):
    #Se considera que se va a usar una variable global, no que pertenezca a la función
    global name1
    global name2
    global name3
    
    ganador.show()
    if (participanteGanador == 0):
        ganadorTexto.clear()
        ganadorTexto.append("Felicitaciones al jugador " + name1 + " por haber ganado")
    elif (participanteGanador == 1):
        ganadorTexto.clear()
        ganadorTexto.append("Felicitaciones al jugador " + name2 + " por haber ganado")
    elif (participanteGanador == 2):
        ganadorTexto.clear()
        ganadorTexto.append("Felicitaciones al jugador " + name3 + " por haber ganado")
    ganadorBoton.text = "EMPEZAR NUEVA PARTIDA"
    app.hide()

def cambiarFondoImagen():
    if (estadoColor == True):
        for i in range(3):
            if (cantJugadores==True and i == 1):
                img = "images/fondoWood.png"
                pictures[i].image = img
                continue
            img = "images/" + str(puntos[i]) + "-wood.png"
            pictures[i].image = img
    else:
        for i in range(3):
            if (cantJugadores==True and i == 1):
                img = "images/fondoDark.png"
                pictures[i].image = img
                continue
            img = "images/" + str(puntos[i]) + "-dark.png"
            pictures[i].image = img

def cambiarImagen(imagen, jugador):
    #Se pone con fondo dark
    if (estadoColor == True):
        #print("Se pone con fondo dark")
        img = "images/" + str(puntos[jugador]) + "-dark.png"
        imagen.image = img
    else:
        #print("Se pone con fondo forest")
        img = "images/" + str(puntos[jugador]) + "-wood.png"
        imagen.image = img

def sumarPuntosJug1():
    print(puntos[0])
    if (aPuntos == True):
        puntoTotale = 15
    else:
        puntoTotale = 30
    if (puntos[0] <= puntoTotale):
        if (puntos[0] == puntoTotale):
            #No se hace nada
            print("Se está en la victoria")
        else:
            puntos[0] += 1
            cambiarImagen(pictures[0], 0)
        gano(puntos[0], 0)

def sumarPuntosJug2():
    if (cantJugadores == True):
        return
    print("Los puntos del participante 2 son" + str(puntos[1]))
    if (aPuntos == True):
        puntoTotale = 15
    else:
        puntoTotale = 30
    if (puntos[1] < puntoTotale):
        if (puntos[1] == puntoTotale):
            #No se hace nada
            print("Se está en la victoria")
        else:
            puntos[1] += 1
            cambiarImagen(pictures[1], 1)
        gano(puntos[1], 1)

def sumarPuntosJug3():
    print("Se suma 1 punto al jugador 3")
    if (aPuntos == True):
        puntoTotale = 15
    else:
        puntoTotale = 30
    if (puntos[2] < puntoTotale):
        if (puntos[0] == puntoTotale):
            #No se hace nada
            print("Se está en la victoria")
        else:
            puntos[2] += 1
            cambiarImagen(pictures[2], 2)
        gano(puntos[2], 2)

def restarPuntosJug1():
    if puntos[0] > 0:
        puntos[0] -= 1
        cambiarImagen(pictures[0], 0)
        print("Se resta 1 punto al jugador 1")

def restarPuntosJug2():
    if (cantJugadores == True):
        return
    if puntos[1] > 0:
        puntos[1] -= 1
        cambiarImagen(pictures[1], 1)
        print("Se resta 1 punto al jugador 2")

def restarPuntosJug3():
    if puntos[2] > 0:
        puntos[2] -= 1
        cambiarImagen(pictures[2], 2)
        print("Se resta 1 punto al jugador 3")

def cambiarNombre1():
    if (envidoButton.value == "Flor"):
        envido.text = "3 pts"
        envidoDoble.text = "4 pts"
        realEnvido.text = "6 pts"
        faltaEnvido.text = "Flor al resto"
    else:
        envido.text = "Envido"
        envidoDoble.text = "Envido"
        realEnvido.text = "Real Envido"
        faltaEnvido.text = "Falta envido"

#Se devuelve 1 si gano
#Si perdió se devuelve 0
def gano(puntos, participante):
    if (aPuntos == False):
        if (puntos >= 30):
            print("Gano el participante " + str(participante))
            #respuesta = yesno("Nueva partida", "Se empieza nueva partida?")
            ganoPartida(participante)
            #inicializarVariables()
    else:
        if (puntos >= 15):
            print("Gano el participante " + str(participante))
            #respuesta = yesno("Nueva partida", "Se empieza nueva partida?")
            ganoPartida(participante)
            #inicializarVariables()
    return 0

def inicializarVariables():
    ganador.hide()
    puntos[0] = 0
    puntos[1] = 0
    puntos[2] = 0
    #Se ponen las imagenes del principio
    for i in pictures:
        cambiarImagen(i, 0)
    empezarPartida()

def empezarPartida():

    global cantJugadores
    global flor
    global aPuntos
    global name1
    global name2
    global name3
    app.hide()

    #Hace un pop-up que deja responder SI o NO al usuario unicamente
    cantJugadores = yesno("Jugadores", "son 2 jugadores")
    if (cantJugadores==True):
        nombre1.clear()

        #Se pregunta sobre como se llama en un pop-up que permite ingresar texto
        name1 = question("Jugador 1", "Cómo se llama", initial_value=None)
        nombre1.append(name1)

        nombre3.clear()
        name2 = question("Jugador 2", "Cómo se llama", initial_value=None)
        nombre3.append(name2)
        pictures[1].bg = darkColor[3]
        pictures[1].image = "images/fondoDark.png"

        #Saca a un elemento de una lista de un objeto Combo
        trucoPart.remove("Jugador Dos")
        envidoPart.remove("Jugador Dos")

        #Oculta los botones
        addPointsPlayer2.hide()
        substractPointsPlayer2.hide()
    else:
        nombre1.clear()
        #Permite al usuario 
        name1 = question("Jugador 1", "Cómo se llama", initial_value=None)
        nombre1.append(name1)
        
        nombre2.clear()
        name2 = question("Jugador 2", "Cómo se llama", initial_value=None)
        nombre2.append(name2)

        name3 = question("Jugador 3", "Cómo se llama", initial_value=None)
        nombre3.clear()
        nombre3.append(name3)

        trucoPart.remove("Jugador Dos")
        envidoPart.remove("Jugador Dos")
        trucoPart.insert(2, "Jugador Dos")
        envidoPart.insert(2, "Jugado Dos")

    
    flor = yesno("Flor", "Se juega con flor?")

    if (flor == True):
        envidoButton.remove("Flor")
        envidoButton.insert(1, "Flor")
    else:
        envidoButton.remove("Flor")
    aPuntos = yesno("Puntos", "Se juega a 15?")
    app.show()


#Función llamada cuando se pulsa el boton de SUMAR PUNTOS
def sumarPuntos():

    #Primero, se tiene que ver si se canto falta envido, luego si se gano con envido y luego con truco
    point = sumarPuntosCorrectos()
    if (point == -1):
        return
    if (hayEnvidoFlor == -1):
        defectoEnvido()
    else:
        sumarEnvido()
        defectoEnvido()
    for i in range(3):
        num = gano(puntos[i], i)
        if (num == 1):
            return

    tru = sumarTruco()
    for i in range(3):
        gano(puntos[i], i)
    #Se fija si había truco o no
    if (tru == 0):
        defectoEnvido()
        return 
    for i in range(3):
        if (cantJugadores == True and i == 1):
            continue
        cambiarImagen(pictures[i], i)
    
    
#Devuelve 1 si está correcto
#Devuelve -1 si está mal
def sumarPuntosCorrectos():

    #Se busca en que posición de la lista está el item
    partPos = participante.index(trucoPart.value)
    cantoTruco = cantosTruco.index(trucoEleccion.value)

    #Si es la primer posición, no se eligió nada
    if partPos == 0 or cantoTruco == 0:
        return -1
    return 1

#Devuelve 1 si hay
#Devuelve -1 si no hay
def hayEnvidoFlor():
    partPos = participante.index(envidoPart.value)
    if (partPos == 0):
        return -1
    if envido.value == 0 and envidoDoble.value == 0 and realEnvido.value == 0 and faltaEnvido == 0:
        return -1
    return 1
    

#Función que calcula lo del truco
def sumarTruco():
    partPos = participante.index(trucoPart.value)
    cantoTruco = cantosTruco.index(trucoEleccion.value)

    #Se vuelve a su posicion original
    trucoEleccion.value = cantosTruco[0]
    trucoPart.value = participante[0]
    #print(partPos)
    #print(cantoTruco)

    #Si ninguna de las 2 estaba seleccionada, no se hace nada. Está mal
    if partPos == 0 or cantoTruco == 0:
        return 0
    
    #Se verifica cual opción ha sido seleccionada
    if cantoTruco == 1:
        #print("Nada")
        puntos[partPos - 1] += 1
    elif cantoTruco == 2:
        #print("Truco")
        puntos[partPos - 1] += 2
    elif cantoTruco == 3:
        puntos[partPos - 1] += 3
        #print("Retruco")
    elif cantoTruco == 4:
        puntos[partPos - 1] += 4
        #print("Value cuatro")
    return 1

#Función que calcula el envido
def sumarEnvido():
    
    #Se calcula el número de participante
    partPos = participante.index(envidoPart.value)

    #Se vuelve al valor original
    envidoPart.value = participante[0]
    
    #Variables
    envidos = []
    florTantos = []
    res = True

    # Se calcula que se canto
    # En caso de envido es 2
    # En caso de real envido es 3
    # En caso de falta envido es -1
    if (envidoButton.value == "Envido"):
        if (envido.value == 1):
            envidos.append(2)
            print("Hay envido")
        if (envidoDoble.value == 1):
            envidos.append(2)
            print("Hay doble envido")
        if (realEnvido.value == 1):
            envidos.append(3)
            print("Hay real envido")
        if (faltaEnvido.value == 1):
            print("Hay falta envido")
            envidos.append(-1)

        #Si hay uno solo, averiguar si se quiso o no
        if (len(envidos) == 1):
            res = yesno("Envido", "Quiso?")

        #Si la respuesta es Falsa (no), entonces sumar 1 punto
        if (res == False):
            puntos[partPos - 1] += 1

    #Si es verdadera, sumar todos los puntos, mientras que no haya falta envido
        else:
            if (-1 not in envidos):
                for i in envidos:
                    puntos[partPos - 1] += i

            #Se calcula el falta envido
            else:
                maximo = -1
                for i in range(len(puntos)):
                    if (maximo <= puntos[i]):
                        maximo = puntos[i]
                if (maximo <= 15):
                    if (aPuntos == True):
                        puntos[partPos - 1] = 15
                    else:
                        puntos[partPos - 1] = 30
                else:
                    puntos[partPos-1] += 30 - maximo

    #se jugo por flor
    else:
        if (faltaEnvido.value == 1):
            print("Hay flor al resto")
            florTantos.append(-1)
        if (realEnvido.value == 1):
            flor.append(6)
            print("Hay 6 pts")
        if (envidoDoble.value == 1):
            florTantos.append(4)
            print("Hay recontra flor 6pts")
        if (envido.value == 1):
            florTantos.append(3)
            print("Hay flor")
        
        #Verificar si se jugó por al resto
        if (-1 in florTantos):
            res = yesno("Al resto", "Quiso?")
            if (res == False):
                puntos[partPos - 1] += 6
            else:
                #Se calcula cual es el maximo
                maximo = -1
                for i in range(len(puntos)):
                    if (maximo <= puntos[i]):
                        maximo = puntos[i]
                #Se gana directamente si es menor a 15
                if (maximo <= 15):
                    if (aPuntos == True):
                        puntos[partPos - 1] = 15
                    else:
                        puntos[partPos - 1] = 30
                #Si es mayor a 15, entonces, se juega a lo que falta al que va ganando
                else:
                    puntos[partPos-1] += 30 - maximo
        else:
            if (6 in florTantos):
                puntos[partPos-1] += 6
            elif (4 in florTantos):
                puntos[partPos-1] += 4
            elif (3 in florTantos):
                puntos[partPos-1] += 3

def defectoEnvido():
    #Se cambian todos los valores del envido a 0 (se "destildan")
    envido.value = 0
    envidoDoble.value = 0
    realEnvido.value = 0
    faltaEnvido.value = 0
    envidoPart.value = participante[0]
    envidoButton.value = juego[0]

#Función llamada al presionar una tecla
def keys(event):
    print("Hola mundo")
# yA ENTEDI AHORA TE AYUDO

def cambiarColor():
    #Se cambia de estado
    global estadoColor # Esto que puse acá es porque es una variable global, sino me tira error
    global app
    global titulo
    global nombre1
    global nombre2
    global nombre3

    #Se cambia el fondo de las imagenes
    cambiarFondoImagen()

    #se intercambia entre true y false
    if (estadoColor == True):
        estadoColor = False
    else:
        estadoColor = True
    
    
    #Se cambia de color
    if (estadoColor == True):
        ##luego, aca quiero que se pongan los colores en base a la lista de colores dark
        print("Se cambia al tema dark")
        #Copie todos los colores y les pongo un color en base a la lista
        app.bg = darkColor[2]
        titulo.bg = darkColor[0]
        titulo.text_color = darkColor[4]
        nombre1.bg = darkColor[3]
        nombre2.bg = darkColor[3]
        nombre3.bg = darkColor[3]

        botonCambiarColor.tk.config(bg=darkColor[3])
        addPointsPlayer1.tk.config(bg=darkColor[3])
        substractPointsPlayer1.tk.config(bg=darkColor[3])

        addPointsPlayer2.tk.config(bg=darkColor[3])
        substractPointsPlayer2.tk.config(bg=darkColor[3])

        addPointsPlayer3.tk.config(bg=darkColor[3])
        substractPointsPlayer3.tk.config(bg=darkColor[3])
        
        botomSumar.tk.config(bg=darkColor[3])

        envidoButton.bg = darkColor[3]
        envidoPart.bg = darkColor[3]

        trucoPart.bg = darkColor[3]
        trucoEleccion.bg = darkColor[3]
    if (estadoColor == False):
        print("Se cambia al tema forest")
        app.bg = forestColor[0]
        titulo.bg = forestColor[1]
        titulo.text_color = forestColor[3]
        nombre1.bg = forestColor[3]
        nombre2.bg = forestColor[3]
        nombre3.bg = forestColor[3]

        botonCambiarColor.tk.config(bg=forestColor[3])
        addPointsPlayer1.tk.config(bg=forestColor[4])
        substractPointsPlayer1.tk.config(bg=forestColor[4])

        addPointsPlayer2.tk.config(bg=forestColor[4])
        substractPointsPlayer2.tk.config(bg=forestColor[4])

        addPointsPlayer3.tk.config(bg=forestColor[4])
        substractPointsPlayer3.tk.config(bg=forestColor[4])

        botomSumar.tk.config(bg=forestColor[4])

        envidoButton.bg = forestColor[4]
        envidoPart.bg = forestColor[4]

        trucoPart.bg = forestColor[4]
        trucoEleccion.bg = forestColor[4]

#Variablles
participante = ["(Elegir opcion)","Jugador Uno","Jugador Dos", "Jugador Tres"]
cantosTruco = ["(Elegir opcion)", "Nada","Truco","Retruco","Vale cuatro"]
cantosEnvido = ["(Elegir opcion)","Envido","Real envido","Falta envido"]
juego = ["Envido", "Flor"]
puntos = [0, 0, 0]

#COLORES
darkColor = [
    "#404258",
    "#474E68",
    "#50577A",
    "#6B728E",
    "#C0BAD6"
] ##Estos son los colores dark

forestColor = [
    "#3A4D39",
    "#4F6F52",
    "#ECE3CE",
    "#A47E3B",
    "#61481C"
]

#Variables de nombres de los participantes
name1 = ""
name2 = ""
name3 = ""

#Cantidad de jugadores
cantJugadores = True

flor = True
aPuntos = True
estadoColor = False

#top
topHeight = 75

#middle
middleBoxTopHeight = 40
middleBoxPictureHeight = 260
middleHeight = middleBoxTopHeight + middleBoxPictureHeight

#bottom
bottomHeightButtonPlayer = 50
bottomHeightTruco = 100
bottomHeightEnvido = 100
bottomHeightAdd = 50
bottomHeight = 50

#padding width
paddingRight = 50
paddingLeft = 50

#center wdith
center = 400
thirdWidth = int(center/3)
thirdWidthChar = int(thirdWidth / 8)
buttonsWidth = int(thirdWidthChar / 3)
paddingButtonWidth = thirdWidthChar - buttonsWidth * 2

paddingComboWidth = 15
comboWidth = int((center - paddingComboWidth * 2) / 8 / 3.32)


#CAMBIARLO CUANDO NO QUIERO QUE APAREZCAN LOS BORDES
border = False

#Se inicializa la aplicacion y se le da fondo, altura y ancho
app = App("Anotador de truco", bg=darkColor[2])
app.height = topHeight + middleHeight + bottomHeight + bottomHeightTruco + bottomHeightEnvido + bottomHeightAdd
app.width = paddingRight + paddingLeft + center

#Top box
topBox = Box(app, align="top", width= "fill", height= topHeight, border= border)
botonCambiarColor = PushButton(topBox, align="left", height="fill", text="Cambiar tema", command=cambiarColor)
titulo = Text(topBox, "Anotador de truco", width="fill", color=darkColor[4], height="fill", align="top", bg=darkColor[0])

#Middle box
middleBox = Box(app, align="top", width= "fill", height = middleHeight, border= border)
paddingCenterLeft = Box(middleBox, width=paddingLeft, height=middleHeight, border=border, align="left")
paddingCenterLeft = Box(middleBox, width=paddingLeft, height=middleHeight, border=border, align="right")

#Middle box top
middleBoxTop = Box(middleBox, align="top", width= "fill", height = middleBoxTopHeight, border= border)
nombre1 = Text(middleBoxTop, width="fill", align="left", text="", bg=darkColor[3])
nombre2 = Text(middleBoxTop, width="fill", align="left", text="", bg=darkColor[3])
nombre3 = Text(middleBoxTop, width="fill", align="left", text="", bg=darkColor[3])

#Middle box picture

middleBoxPicture = Box(middleBox, align="top", width= "fill", height = middleBoxPictureHeight, border= border)

pictures = [
Picture(middleBoxPicture, image="images/0-wood.png", width=thirdWidth, height=middleBoxPictureHeight, align="left"),
Picture(middleBoxPicture, image="images/0-wood.png", width=thirdWidth, height=middleBoxPictureHeight, align="left"),
Picture(middleBoxPicture, image="images/0-wood.png", width=thirdWidth, height=middleBoxPictureHeight, align="rigth")
]
#Bottom box picture
bottomBox = Box(app, align="top", width= "fill", height = bottomHeight, border= border)
paddingCenterLeft = Box(bottomBox, width=paddingLeft, height="fill", border=border, align="left")
paddingCenterLeft = Box(bottomBox, width=paddingLeft, height="fill", border=border, align="right")

#Create boxes for players
bottomBoxButtons = Box(bottomBox, align="top", width= "fill", height = bottomHeight, border= border)
bottomBoxButtonsPlayer1 = Box(bottomBoxButtons, align="left", width= thirdWidth, height = bottomHeightButtonPlayer, border= border)
bottomBoxButtonsPlayer2 = Box(bottomBoxButtons, align="left", width= thirdWidth, height = bottomHeightButtonPlayer, border= border)
bottomBoxButtonsPlayer3 = Box(bottomBoxButtons, align="left", width= thirdWidth, height = bottomHeightButtonPlayer, border= border)
addButtons = []

#Player 1
paddingButton = Box(bottomBoxButtonsPlayer1, width=paddingButtonWidth, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxButtonsPlayer1, width=paddingButtonWidth, height="fill", border=border, align="right")
addPointsPlayer1 = PushButton(bottomBoxButtonsPlayer1, width= buttonsWidth, height="fill", text="+", align="left", command=sumarPuntosJug1)
substractPointsPlayer1 = PushButton(bottomBoxButtonsPlayer1, width= buttonsWidth, height="fill", text="-", align="right", command=restarPuntosJug1)



#Player 2
paddingButton = Box(bottomBoxButtonsPlayer2, width=paddingButtonWidth, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxButtonsPlayer2, width=paddingButtonWidth, height="fill", border=border, align="right")
addPointsPlayer2 = PushButton(bottomBoxButtonsPlayer2, width= buttonsWidth, height="fill", text="+", align="left", command=sumarPuntosJug2)
substractPointsPlayer2 = PushButton(bottomBoxButtonsPlayer2, width= buttonsWidth, height="fill", text="-", align="right", command=restarPuntosJug2)

#Player 3
paddingButton = Box(bottomBoxButtonsPlayer3, width=paddingButtonWidth, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxButtonsPlayer3, width=paddingButtonWidth, height="fill", border=border, align="right")
addPointsPlayer3 = PushButton(bottomBoxButtonsPlayer3, width= buttonsWidth, height="fill", text="+", align="left", command=sumarPuntosJug3)
substractPointsPlayer3 = PushButton(bottomBoxButtonsPlayer3, width= buttonsWidth, height="fill", text="-", align="right", command=restarPuntosJug3)

#Truco
bottomBoxTruco = Box(app, align="top", width= "fill", height = bottomHeightTruco, border=border)
paddingButton = Box(bottomBoxTruco, width=paddingLeft, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxTruco, width=paddingRight, height="fill", border=border, align="right")
trucoButton = Text(bottomBoxTruco, width=comboWidth, height="fill", text="TRUCO", align="left")
paddingCombo = Box(bottomBoxTruco, width=paddingComboWidth, height="fill", border=border, align="left")
trucoPart = Combo(bottomBoxTruco, width=comboWidth, height="fill", options=participante, align = "left")
paddingCombo = Box(bottomBoxTruco, width=paddingComboWidth, height="fill", border=border, align="left")
trucoEleccion = Combo(bottomBoxTruco, width=comboWidth, height="fill", options=cantosTruco, align="left")

#Envido // Flor
bottomBoxEnvido = Box(app, align="top", width= "fill", height = bottomHeightEnvido, border=border)
paddingButton = Box(bottomBoxEnvido, width=paddingLeft, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxEnvido, width=paddingRight, height="fill", border=border, align="right")
envidoButton = Combo(bottomBoxEnvido, width=comboWidth, height="fill", options=juego, align="left", command=cambiarNombre1)
paddingCombo = Box(bottomBoxEnvido, width=paddingComboWidth, height="fill", border=border, align="left")
envidoPart = Combo(bottomBoxEnvido, width=comboWidth, height="fill", options=participante, align = "left")
paddingCombo = Box(bottomBoxEnvido, width=paddingComboWidth, height="fill", border=border, align="left")

#Se crea una lista de checkboxes para calcular que se ha jugado
envidoEleccion = Box(bottomBoxEnvido, width="fill", height="fill", border=border, align="left")
envido = CheckBox(envidoEleccion, text="Envido", width="fill", align="top")
envidoDoble = CheckBox(envidoEleccion, text="Envido", align="top", width="fill")
realEnvido = CheckBox(envidoEleccion, text="Real Envido", align="top", width="fill")
faltaEnvido = CheckBox(envidoEleccion, text="Falta Envido", align="top", width="fill")

#Add 
bottomBoxAdd = Box(app, align="top", width= "fill", height = bottomHeightAdd, border=border)
paddingButton = Box(bottomBoxAdd, width=paddingLeft, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxAdd, width=paddingRight, height="fill", border=border, align="right")
botomSumar = PushButton(bottomBoxAdd, width= int(center / 8 / 3), height="fill", text="SUMAR PUNTOS", command=sumarPuntos)

#Functionalities
pictures[0].when_clicked = sumarPuntosJug1
pictures[1].when_clicked = sumarPuntosJug2
pictures[2].when_clicked = sumarPuntosJug3
pictures[0].when_right_button_pressed = restarPuntosJug1
pictures[1].when_right_button_pressed = restarPuntosJug2
pictures[2].when_right_button_pressed = restarPuntosJug3
app.when_key_released = keys

#Configure the fonts
titulo.tk.config(font=("Georgia", 32))

nombre1.tk.config(font=("Cambria", 8))
nombre2.tk.config(font=("Cambria", 8))
nombre3.tk.config(font=("Cambria", 8))

envidoButton.tk.config(font=("Cambria", 10))
trucoButton.tk.config(font=("Cambria", 12))

botomSumar.tk.config(font=("impact", 15))

#Alternative windows
ganador = Window(app, title="Ganador", width=600, height=400)
ganadorTexto = Text(ganador, align="top", width="fill", height=10, size=20, text="")
ganadorBoton = PushButton(ganador, text="", command=inicializarVariables)
ganador.hide()

#Sets the app not resizable
app.tk.resizable(height = 0, width=0)

cambiarColor()
inicializarVariables()
app.display()
