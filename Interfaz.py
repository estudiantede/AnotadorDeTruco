from guizero import App, Text, TextBox, Box, Combo, Picture, PushButton, Slider

puntos = [0, 0]

def SumarPunto (num):
    #print("Hola mundo")
    if num==0:
        puntos[0] += 1
        puntosJug1.value = str(puntos[0])
    elif num==1:
        puntos[1] += 1
        puntosJug2.value = str(puntos[1])

cantosTruco = ["(Elegir opcion)", "Nada","Truco", "Retruco", "Vale cuatro"]

cantosEnvido = ["(Elegir opcion)", "Envido","Real envido", "Falta envido"]

ventana = App("Anotador de truco", height=700, bg="#FFFFFF")
titulo = Text(ventana, "Anotador de truco", size=30, width="fill", color="#FFBBCC", height=3, align="top")
centerBox = Box(ventana, layout="grid")

nombre1 = TextBox(centerBox, width="fill", grid = [0, 0])
nombre2 = TextBox(ventana, width="fill")

#imagenJug1 = Picture(ventana, image="images/1.jpeg")
#imagenJug2 = Picture(ventana, image="images/1.jpeg")

puntosJug1 = Text(ventana, text="0")
puntosJug2 = Text(ventana, text="0")

sumarPuntosJug1 = PushButton(ventana, command=SumarPunto, args=[0])
sumarPuntosJug2 = PushButton(ventana, command=SumarPunto, args=[1])
jug1 = Combo(ventana, options=cantosTruco)
jug2 = Combo(ventana, options=cantosEnvido)

ventana.display()

from guizero import App, Text, TextBox, Box, Combo, Picture, PushButton, Slider

puntos = [0, 0]

def SumarPunto (num):
    #print("Hola mundo")
    if num==0:
        puntos[0] += 1
        puntosJug1.value = str(puntos[0])
    elif num==1:
        puntos[1] += 1
        puntosJug2.value = str(puntos[1])

cantosTruco = ["(Elegir opcion) ⬇️", "Nada","Truco","Retruco","Vale cuatro"]
cantosEnvido = ["(Elegir opcion) ⬇️","Envido","Real envido","Falta envido"]
participante = ["(Elegir opcion) ⬇️","Jugador Uno","Jugador Dos"]
ventana = App("Anotador de truco", height=700, bg="#FFFFFF")

titulo = Text(ventana, "Anotador de truco", size=30, width="fill", color="#FFBBCC", height=3, align="top")
centerBox1 = Box(ventana, width="fill", border=True)
centerBox2 = Box(ventana, width="fill", border=True)
centerBox3 = Box(ventana, width="fill", border=True)
centerBox4 = Box(ventana, width="fill", border=True)

nombre1 = TextBox(centerBox1, width="fill", align="left")
nombre2 = TextBox(centerBox1, width="fill", align="right")

#imagenJug1 = Picture(ventana, image="images/1.jpeg")
#imagenJug2 = Picture(ventana, image="images/1.jpeg")

puntosJug1 = Text(centerBox2, text="0", align="left")
puntosJug2 = Text(centerBox2, text="0", align="right")

sumarPuntosJug1 = PushButton(centerBox3, command=SumarPunto, args=[0], align="left")
sumarPuntosJug2 = PushButton(centerBox3, command=SumarPunto, args=[1], align="right")
jug1 = Combo(centerBox4, options=cantosTruco, align="left")
jug2 = Combo(centerBox4, options=cantosEnvido, align="right")
wchos = Combo(ventana, options=participante)
Puntos = PushButton(ventana, command=SumarPunto, args=[1])

ventana.display()

from guizero import App, Text, TextBox, Box, Combo, Picture, PushButton, Slider

puntos = [0, 0]

def SumarPunto (num):
    #print("Hola mundo")
    if num==0:
        puntos[0] += 1
        puntosJug1.value = str(puntos[0])
    elif num==1:
        puntos[1] += 1
        puntosJug2.value = str(puntos[1])

cantosTruco = ["(Elegir opcion) ⬇️", "Nada","Truco","Retruco","Vale cuatro"]
cantosEnvido = ["(Elegir opcion) ⬇️","Envido","Real envido","Falta envido"]
participante = ["(Elegir opcion) ⬇️","Jugador Uno","Jugador Dos"]
ventana = App("Anotador de truco", height=700, bg="#FFFFFF")

titulo = Text(ventana, "Anotador de truco", size=30, width="fill", color="#A6F3EB", height=1, align="top")

centerBox1 = Box(ventana, width="fill", border=True, height=50) 
centerBoxPicture = Box(ventana, width="fill", border=True, height=50) 
centerBox2 = Box(ventana, width="fill", border=True, height=50)
centerBox3 = Box(ventana, width="fill", border=True, height=50)
centerBox4 = Box(ventana, width="fill", border=True, height=50)
centerBox5 = Box(ventana, width="fill", border=True, height=50)

nombre1 = TextBox(centerBox1, width="fill", align="left")
nombre2 = TextBox(centerBox1, width="fill", align="right")

#imagenJug1 = Picture(ventana, image="images/1.jpeg")
#imagenJug2 = Picture(ventana, image="images/1.jpeg")

puntosJug1 = Text(centerBox2, text="0", align="left")
puntosJug2 = Text(centerBox2, text="0", align="right")

sumarPuntosJug1 = PushButton(centerBox3, text="+Puntos", command=SumarPunto, args=[0], align="left")
sumarPuntosJug2 = PushButton(centerBox3, text="+Puntos", command=SumarPunto, args=[1], align="right")
TrucoJug1 = Combo(centerBox4, options=cantosTruco, align="left")
TrucoJug2 = Combo(centerBox4, options=cantosTruco, align="right")

Envidojug1 = Combo(centerBox5, options=cantosEnvido, align="left")
Envidojug2 = Combo(centerBox5, options=cantosEnvido, align="right")
#wchos = Combo(ventana, options=participante)
PuntosJug1 = PushButton(ventana, text="Sumar Puntos", command=SumarPunto, args=[1])

ventana.display()

