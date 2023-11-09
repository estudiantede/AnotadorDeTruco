#Se importa TODAS las librerias
from guizero import *

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
        gano(puntos[0], 0)

def sumarPuntosJug2():
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
        gano(puntos[1], 0)

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
        gano(puntos[2], 0)
        

        # che no encontre mas bg de los que te puse ahí
        #Ahí me fijo
        #ahora te digo
        #Wtf
        #nose se esta bien lo que hice o si m
def restarPuntosJug1():
    if puntos[0] > 0:
        puntos[0] -= 1
        print("Se resta 1 punto al jugador 1")

def restarPuntosJug2():
    if puntos[1] > 0:
        puntos[1] -= 1
        print("Se resta 1 punto al jugador 2")

def restarPuntosJug3():
    if puntos[2] > 0:
        puntos[2] -= 1
        print("Se resta 1 punto al jugador 3")

#Funciones que todavia no hacen nada
def cambiarNombre1():
    if (envidoButton.value == "Flor"):
        envido.text = "Flor"
        envidoDoble.text = "6 pts"
        realEnvido.text = "9 pts"
        faltaEnvido.text = "flor al resto"
    else:
        envido.text = "Envido"
        envidoDoble.text = "Envido"
        realEnvido.text = "Real Envido"
        faltaEnvido.text = "Falta envido"

#Se devuelve 1 si gano
#Si perdió se devuelve 0
def gano(puntos, participante):
    if (aPuntos == True):
        if (puntos >= 15):
            print("Gano el participante " + str(participante))
            respuesta = yesno("Nueva partida", "Se empieza nueva partida?")
            if respuesta == True:
                inicializarVariables()
    else:
        if (puntos >= 30):
            print("Gano el participante " + str(participante))
            respuesta = yesno("Nueva partida", "Se empieza nueva partida?")
            if respuesta == True:
                inicializarVariables()
    return 0

def inicializarVariables():
    puntos[0] = 0
    puntos[1] = 0
    puntos[2] = 0
    empezarPartida()

def empezarPartida():
    app.hide()
    nombre1.clear()
    nombre1.append(question("Jugador 1", "Cómo se llama", initial_value=None))
    nombre2.clear()
    nombre2.append(question("Jugador 2", "Cómo se llama", initial_value=None))
    nombre3.clear()
    nombre3.append(question("Jugador 3", "Cómo se llama", initial_value=None))

    flor = yesno("Flor", "Se juega con flor?")
    aPuntos = yesno("Puntos", "Se juega a 15?")
    app.show()

#Función llamada cuando se pulsa el boton de SUMAR PUNTOS
def sumarPuntos():
    """
    tru = sumarTruco()
    #Se fija si había truco o no
    if (tru == 0):
        defectoEnvido()
        return 
    sumarEnvido()
    defectoEnvido()
    """

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
    if partPos == 0 or cantosTruco == 0:
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
    flor = 0
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
                print("Se calcula el falta envido")
    else:
        if (faltaEnvido.value == 1):
            print("Hay flor al resto")
            flor = -1
        elif (realEnvido.value == 1):
            flor = 9
            print("Hay recontra flor 9 pts")
        elif (envidoDoble.value == 1):
            flor = 6
            print("Hay recontra flor 6pts")
        elif (envido.value == 1):
            flor = 3
            print("Hay flor")
        
        #Verificar que se haya ingresado a algun participante
        if (flor != 0 and envidoPart.value == participante[0]):
            return
        elif (flor == 0):
            return

        if (flor != -1):
            puntos[partPos - 1] += flor
        else:
            print("El participante " + str(partPos) + " ha ganado la partida")

def defectoEnvido():
    #Se cambian todos los valores del envido a 0 (se "destildan")
    envido.value = 0
    envidoDoble.value = 0
    realEnvido.value = 0
    faltaEnvido.value = 0

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

    #Me tira error por eso
    #Bueno, aca lo que hace es cambiar una variable entre false y true, porque quiero que vaya y vuelva
    if (estadoColor == True):
        estadoColor = False
    else:
        estadoColor = True
    
    
    #Se cambia de color
    if (estadoColor == True):
        ##luego, aca quiero que se pongan los colores en base a la lista de colores dark
        print("Se cambia al tema dark")
        #Copie todos los colores y les pongo un color en base a la lista
        app.bg = darkColor[0]
        titulo.bg = darkColor[2]
        nombre1.bg = darkColor[3]
        nombre2.bg = darkColor[3]
        nombre3.bg = darkColor[3]
    if (estadoColor == False):
        print("Se cambia al tema forest")
        app.bg = "blue"
        titulo.bg = "blue"
        nombre1.bg = "blue"
        nombre2.bg = "blue"
        nombre3.bg = "blue"
    #Porque esos también querría cambiarles el color. Tenían bg dentro
    #Despues de esos, c
    # como mas te ayudoreo que no había ninguno más
    #Ahhh me ayudas con el escrito Seba,
    substractPointsPlayer1.tk.config(bg="blue")
    
    #Seba, fijate que sean los que dicen bg no más
    # AHHH YA VA
    #No se que paso que ahora no puede ejecutar el archivo xd
    #MIERDA, TOCASTE ALGO???
    #Voy a cerrar visual, creo que se cerrará el live share
    #Te lo mando de nuevo, en 1 minutos
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
    "#A47E3B ",
    "#61481C"
]

name1 = ""
name2 = ""
name3 = ""
flor = True
aPuntos = True
estadoColor = True
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
nombre1 = Text(middleBoxTop, width="fill", align="left", text="Hola mundo", bg=darkColor[3])
nombre2 = Text(middleBoxTop, width="fill", align="left", text="Hola mundo", bg=darkColor[3])
nombre3 = Text(middleBoxTop, width="fill", align="left", text="Hola mundo", bg=darkColor[3])

#Me refería a estas propiedades
#AHHH ENTENDI TODO RE AL REVES

#Me explique mal
# QUEDAN VARABLES PARA PINTAR 
#O YA TE ENCARGASTE VOS???

#No, ya están pintadas, pero quería agregarle la funcionalidad de que cambien de color al presionar un boton
#Por eso era que te pedía que las copies las variables en la función aquella

#Middle box picture

middleBoxPicture = Box(middleBox, align="top", width= "fill", height = middleBoxPictureHeight, border= border)

pictures = [
Picture(middleBoxPicture, image="images/bk.jpg", width=thirdWidth, height=middleBoxPictureHeight, align="left"),
Picture(middleBoxPicture, image="images/bk.jpg", width=thirdWidth, height=middleBoxPictureHeight, align="left"),
Picture(middleBoxPicture, image="images/bk.jpg", width=thirdWidth, height=middleBoxPictureHeight, align="left")
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
envido = CheckBox(envidoEleccion, text="Envido         ", width="fill", align="top")
envidoDoble = CheckBox(envidoEleccion, text="Envido         ", align="top", width="fill")
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
#ganador = Window(app, title="Ganador", width=400, height=400)


#Sets the app not resizable
app.tk.resizable(height = 0, width=0)

#Change the button's background-color to blue
substractPointsPlayer1.tk.config(bg="blue")

inicializarVariables()
app.display()
