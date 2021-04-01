from tkinter import *

class ScreenCenter:

    def center(self, parent, width, height):
        positionRight = int((parent.winfo_screenwidth() / 2) - (width / 2))
        # Se calculó que la barra de tarea tiene 18 unidades de alto
        # Falta probarlo en diferentes entornos gráficos
        positionDown = int((parent.winfo_screenheight()/2) - (height/2) - 18)
        parent.geometry("+{}+{}".format(positionRight, positionDown))
