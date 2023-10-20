from guizero import App, Text, TextBox, Box, Combo, Picture, PushButton, Slider


ventana = App("Hola mundo", height=500, bg="#FFFFFF")
titulo = Text(ventana, "Anotador de truco", size=30, width="fill", color="#FFBBCC", height=3)
nombre1 = TextBox(ventana, width="fill", height=2)
nombre2 = TextBox(ventana, width="fill", height=2)

ventana.display()