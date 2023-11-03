from guizero import App, Text, TextBox, Box, Combo, Picture, PushButton, Slider
import funciones
puntos = [0, 0]

def sumarPuntosJug1():
    puntos[0] += 1
    puntosJug1.value = str(puntos[0])

def restarPuntosJug1():
    if puntos[0] > 0:
        puntos[0] -= 1
        puntosJug1.value = str(puntos[0])

def sumarPuntosJug2():
    puntos[1] += 1
    puntosJug2.value = str(puntos[1])

def restarPuntosJug2():
    if puntos[1] > 0:
        puntos[1] -= 1
        puntosJug2.value = str(puntos[1])

def faltaEnvido():
    print("hola mundo")

def SumarPunto (num):
    #print("Hola mundo")
    if num==0:
        puntos[0] += 1
        puntosJug1.value = str(puntos[0])
    elif num==1:
        puntos[1] += 1
        puntosJug2.value = str(puntos[1])

def keys(event):
    if(event.keycode == 18): #cuando se presiona alt
        print("hola")

cantosTruco = ["(Elegir opcion) ⬇️", "Nada","Truco","Retruco","Vale cuatro"]
cantosEnvido = ["(Elegir opcion) ⬇️","Envido","Real envido","Falta envido"]
participante = ["(Elegir opcion) ⬇️","Jugador Uno","Jugador Dos"]
ventana = App("Anotador de truco", height=700, bg="#FFFFFF")

titulo = Text(ventana, "Anotador de truco", size=30, width="fill", color="#A6F3EB", height=1, align="top")

centerBox1 = Box(ventana, width="fill", height=50) 
centerBoxPicture = Box(ventana, width="fill", height=50) 
centerBox2 = Box(ventana, width="fill", height=50)
centerBox3 = Box(ventana, width="fill", height=50)
centerBox4 = Box(ventana, width="fill", height=50)
centerBox5 = Box(ventana, width="fill", height=50)

nombre1 = TextBox(centerBox1, width="25", align="left")
nombre2 = TextBox(centerBox1, width="25", align="right")

#imagenJug1 = Picture(ventana, image="images/1.jpeg")
#imagenJug2 = Picture(ventana, image="images/1.jpeg")

puntosJug1 = Text(centerBox2, text="0", align="left")
puntosJug2 = Text(centerBox2, text="0", align="right")



agregarPuntosJug2 = PushButton(centerBox3, text="+Puntos", command=sumarPuntosJug1, align="left")
agregarPuntosJug1 = PushButton(centerBox3, text="+Puntos", command=sumarPuntosJug2, align="right")
TrucoJug1 = Combo(centerBox4, options=cantosTruco, align="left")
TrucoJug2 = Combo(centerBox4, options=cantosTruco, align="right")

Envidojug1 = Combo(centerBox5, options=cantosEnvido, align="left")
Envidojug2 = Combo(centerBox5, options=cantosEnvido, align="right")
#wchos = Combo(ventana, options=participante)

puntosJug1.when_clicked = sumarPuntosJug1
puntosJug2.when_clicked = sumarPuntosJug2

puntosJug1.when_right_button_pressed = restarPuntosJug1
puntosJug2.when_right_button_pressed = restarPuntosJug2

ventana.when_key_released = keys

ventana.display()