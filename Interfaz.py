from guizero import App, Text

ventana = App("Hola mundo", height=200, bg="#FFFFFF")
texto = Text(ventana, "Esto es un texto")


ventana.display()