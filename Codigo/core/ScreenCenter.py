from tkinter import *

"""
Clase que permite el centrado de las ventanas.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class ScreenCenter:

    """
    Función que contiene las formulas necesarias para realizar el centrado
    de todas las pantallas.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def center(self, parent, width, height):
        xCoordinate = int(parent.winfo_screenwidth()/2 - width/2)
        yCoordinate = int(parent.winfo_screenheight()/2 - height/2)
        parent.geometry('+%d+%d' % (xCoordinate, yCoordinate))