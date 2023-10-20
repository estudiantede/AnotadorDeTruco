from guizero import App, Text, TextBox, Box, Combo, Picture, PushButton, Slider

def SumarPunto (num):
    #print("Hola mundo")
    if num==1:
        puntosJug1.value = "1"
    elif num==2:
        puntosJug2.value = "1"

cantosTruco = ["(Elegir opcion)", "Nada","Truco", "Retruco", "Vale cuatro"]

cantosEnvido = ["(Elegir opcion)", "Envido","Real envido", "Falta envido"]

ventana = App("Anotador de truco", height=700, bg="#FFFFFF")
titulo = Text(ventana, "Anotador de truco", size=30, width="fill", color="#FFBBCC", height=3)

nombre1 = TextBox(ventana, width="fill")
nombre2 = TextBox(ventana, width="fill")

imagenJug1 = Picture(ventana, image="images/1.jpeg")
imagenJug2 = Picture(ventana, image="images/1.jpeg")

puntosJug1 = Text(ventana, text="0")
puntosJug2 = Text(ventana, text="0")

sumarPuntosJug1 = PushButton(ventana, command=SumarPunto, args=[1])
sumarPuntosJug2 = PushButton(ventana, command=SumarPunto, args=[2])
jug1 = Combo(ventana, options=cantosTruco)
jug2 = Combo(ventana, options=cantosEnvido)

ventana.display()