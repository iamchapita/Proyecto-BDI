# -*- coding: utf-8 -*-
from tkinter import *

"""
Clase Tooltip muestra las sugerencias al sobre poner el mouse sobre el objeto.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class Tooltip(object):

    
    # Constructor de la clase.
    def __init__(self, widget, text: str):
        # Milisegundos
        self.waittime = 500
        # Pixeles     
        self.wraplength = 180   
        self.widget = widget
        self.text = text
        # Se manejan los eventos siguientes y se designa su respectiva acción
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    # Obtiene el id del evento
    # El evento se maneja con la función after
    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    # Cancela el evento de mostrar el tooltip
    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    # Función que muestra la sugerencia.
    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, wraplength=self.wraplength)
        label.configure(justify='left', bg="white", fg = "black", relief='solid', borderwidth=1,)
        label.pack(ipadx=1)

    # Esconde la sugerencia despues de cierto tiempo.
    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()