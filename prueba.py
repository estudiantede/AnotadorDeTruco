#Se importa las librerias
from guizero import *

#Variablles
participante = ["(Elegir opcion) ⬇️","Jugador Uno","Jugador Dos"]
cantosTruco = ["(Elegir opcion) ⬇️", "Nada","Truco","Retruco","Vale cuatro"]
cantosEnvido = ["(Elegir opcion) ⬇️","Envido","Real envido","Falta envido"]

#top
topHeight = 75

#middle
middleBoxTopHeight = 40
middleBoxPictureHeight = 260
middleHeight = middleBoxTopHeight + middleBoxPictureHeight

#bottom
bottomHeightButtonPlayer = 50
bottomHeightTruco = 50
bottomHeightEnvido = 50
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

comboWidth = int(center / 8 / 4)


#CAMBIARLO CUANDO NO QUIERO QUE APAREZCAN LOS BORDES
border = False
#Se inicializa la aplicacion
app = App("Anotador de truco", bg="#FFFFFF")
app.height = topHeight + middleHeight + bottomHeight + bottomHeightTruco + bottomHeightEnvido + bottomHeightAdd
app.width = paddingRight + paddingLeft + center

#Top box
topBox = Box(app, align="top", width= "fill", height= topHeight, border= border)
titulo = Text(topBox, "Anotador de truco", width="fill", color="#A6F3EB", height="fill", align="top", bg="#FF00FF")
titulo.tk.config(font=("Georgia", 32))


#Middle box
middleBox = Box(app, align="top", width= "fill", height = middleHeight, border= border)
paddingCenterLeft = Box(middleBox, width=paddingLeft, height=middleHeight, border=border, align="left")
paddingCenterLeft = Box(middleBox, width=paddingLeft, height=middleHeight, border=border, align="right")

#Middle box top
middleBoxTop = Box(middleBox, align="top", width= "fill", height = middleBoxTopHeight, border= border)
nombre1 = TextBox(middleBoxTop, width="fill", align="left")
nombre2 = TextBox(middleBoxTop, width="fill", align="left")
nombre3 = TextBox(middleBoxTop, width="fill", align="left")

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
addPointsPlayer1 = PushButton(bottomBoxButtonsPlayer1, width= buttonsWidth, height="fill", text="+", align="left")
substractPointsPlayer1 = PushButton(bottomBoxButtonsPlayer1, width= buttonsWidth, height="fill", text="-", align="right")

#Player 2
paddingButton = Box(bottomBoxButtonsPlayer2, width=paddingButtonWidth, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxButtonsPlayer2, width=paddingButtonWidth, height="fill", border=border, align="right")
addPointsPlayer2 = PushButton(bottomBoxButtonsPlayer2, width= buttonsWidth, height="fill", text="+", align="left")
substractPointsPlayer2 = PushButton(bottomBoxButtonsPlayer2, width= buttonsWidth, height="fill", text="-", align="right")

#Player 3
paddingButton = Box(bottomBoxButtonsPlayer3, width=paddingButtonWidth, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxButtonsPlayer3, width=paddingButtonWidth, height="fill", border=border, align="right")
addPointsPlayer3 = PushButton(bottomBoxButtonsPlayer3, width= buttonsWidth, height="fill", text="+", align="left")
substractPointsPlayer3 = PushButton(bottomBoxButtonsPlayer3, width= buttonsWidth, height="fill", text="-", align="right")

#Truco
bottomBoxTruco = Box(app, align="top", width= "fill", height = bottomHeightTruco, border=border)
paddingButton = Box(bottomBoxTruco, width=paddingLeft, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxTruco, width=paddingRight, height="fill", border=border, align="right")
trucoButton = Text(bottomBoxTruco, width=comboWidth, height="fill", text="TRUCO", align="left", bg="#00FFFF")
trucoPart = Combo(bottomBoxTruco, width=comboWidth, height="fill", options=participante, align="left")
trucoEleccion = Combo(bottomBoxTruco, width=comboWidth, height="fill", options=cantosTruco, align="left")

#Envido 
bottomBoxEnvido = Box(app, align="top", width= "fill", height = bottomHeightEnvido, border=border)
paddingButton = Box(bottomBoxEnvido, width=paddingLeft, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxEnvido, width=paddingRight, height="fill", border=border, align="right")
envidoButton = Text(bottomBoxEnvido, width=comboWidth, height="fill", text="ENVIDO", align="left", bg="#00FFFF")
envidoPart = Combo(bottomBoxEnvido, width=comboWidth, height="fill", options=participante, align="left")
envidoEleccion = Combo(bottomBoxEnvido, width=comboWidth, height="fill", options=cantosEnvido, align="left")


#Add 
bottomBoxAdd = Box(app, align="top", width= "fill", height = bottomHeightAdd, border=border)
paddingButton = Box(bottomBoxAdd, width=paddingLeft, height="fill", border=border, align="left")
paddingButton = Box(bottomBoxAdd, width=paddingRight, height="fill", border=border, align="right")
botomSumar = PushButton(bottomBoxAdd, width= int(center / 8 / 3), height="fill", text="SUMAR PUNTOS")
app.display()