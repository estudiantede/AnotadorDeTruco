from guizero import App, Text, TextBox, Box, Combo, Picture, PushButton, Slider

cantosTruco = ["(Elegir opcion)", "Nada","Truco", "Retruco", "Vale cuatro"]

cantosEnvido = ["(Elegir opcion)", "Envido","Real envido", "Falta envido"]

ventana = App("Hola mundo", height=500, bg="#FFFFFF")
titulo = Text(ventana, "Anotador de truco", size=30, width="fill", color="#FFBBCC", height=3)

nombre1 = TextBox(ventana, width="fill")
nombre2 = TextBox(ventana, width="fill")

imagenJug1 = Picture(ventana, image="images/1.jpeg")
imagenJug2 = Picture(ventana, image="images/1.jpeg")

jug1 = Combo(ventana, options=cantosTruco)
jug2 = Combo(ventana, options=cantosEnvido)

ventana.display()